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

## Repository Structure
