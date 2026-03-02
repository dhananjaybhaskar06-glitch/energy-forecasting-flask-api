
# AI-Powered Energy Consumption Forecasting (MLP + Flask API)

Forecast smart-home energy consumption (kWh) using a machine learning model (MLPRegressor) and deploy it as a Flask REST API for real-time predictions.

## Project Overview
This project predicts **Energy Consumption (kWh)** using:
- Appliance Type
- Outdoor Temperature (°C)
- Season
- Household Size
- Time features derived from Date + Time (hour, day of week, month)

It includes:
- A training notebook (data loading, preprocessing, feature engineering, model training, evaluation)
- A Flask API (`/predict`) that accepts JSON input and returns the predicted kWh

## Tech Stack
- Python
- pandas, numpy
- scikit-learn (Pipeline: StandardScaler + MLPRegressor)
- Flask
- joblib (model persistence)



Activate:
- Windows (PowerShell/CMD):
```bash
.venv\Scripts\activate
```
- macOS/Linux:
```bash
source .venv/bin/activate
```

### 2) Install dependencies
```bash
python -m pip install -r requirements.txt
```

## Run the Flask API
From the project folder (where `app.py` is):
```bash
python app.py
```

API runs at:
- http://127.0.0.1:5000

## API Usage
### Endpoint
`POST /predict`

### Example Request (PowerShell)
```powershell
$body = @{
  home_id = 10
  appliance_type = "TV"
  outdoor_temp = 25.0
  season = "Summer"
  household_size = 3
  hour = 20
  dayofweek = 5
  month = 7
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:5000/predict" -Method Post -ContentType "application/json" -Body $body
```

### Example Response
```json
{
  "predicted_energy_kwh": 3.87
}
```

## Notes
- If you see `InconsistentVersionWarning` from scikit-learn, it means the model was saved with one scikit-learn version and loaded with another. For best results, use the same scikit-learn version used during training, or retrain and resave locally.

## Author
Dhananjay Bhaskar
```
