from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("energy_forecast_mlp.pkl")
cols = joblib.load("energy_forecast_columns.pkl")

def build_row(payload):
    row = pd.DataFrame([{
        "Home ID": payload["home_id"],
        "Outdoor Temperature (°C)": payload["outdoor_temp"],
        "Household Size": payload["household_size"],
        "hour": payload["hour"],
        "dayofweek": payload["dayofweek"],
        "month": payload["month"],
        "Appliance Type": payload["appliance_type"],
        "Season": payload["season"],
    }])

    row = pd.get_dummies(row, columns=["Appliance Type", "Season"], drop_first=True)

    for c in cols:
        if c not in row.columns:
            row[c] = 0

    row = row[cols]
    return row

@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json()

    required = ["home_id", "appliance_type", "outdoor_temp", "season",
                "household_size", "hour", "dayofweek", "month"]
    missing = [k for k in required if k not in payload]
    if missing:
        return jsonify({"error": f"Missing keys: {missing}"}), 400

    X_row = build_row(payload)
    pred = float(model.predict(X_row)[0])
    return jsonify({"predicted_energy_kwh": pred})

if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)

