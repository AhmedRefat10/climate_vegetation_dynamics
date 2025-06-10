# Climate Vegetation Dynamics

This project presents a machine learning and web-based platform for monitoring, forecasting, and supporting adaptive responses to changes in vegetation and wind patterns driven by climate change.

## Problem Statement

Climate change is altering vegetation patterns, rainfall, and wind dynamics, creating both environmental and societal challenges. This project addresses these shifts by building an AI/ML-powered platform that integrates real-time sensor simulation and forecast visualization to support adaptation decisions.

## Project Objectives

- Predict NDVI (vegetation index) and wind conditions using machine learning models
- Simulate real-time environmental sensor data
- Provide actionable adaptation recommendations based on forecasted conditions
- Deliver insights through a web dashboard interface built with Streamlit

## Key Components

### Machine Learning Forecasting

- **NDVI Prediction**: Multi-horizon forecasting (t+1, t+7, t+16, t+30) using XGBoost regression
- **Wind Forecasting**: Wind speed and wind direction forecasts (t+1, t+3, t+7)
- **Feature Engineering**: Includes lag features, rolling statistics, wind vector transformation, and seasonal features
- **Model Evaluation**: RMSE, R² metrics for all forecast horizons

### Adaptation Decision Engine

A rule-based system generates dynamic adaptation advice based on:
- Low NDVI levels
- Insufficient rainfall
- High wind speeds

Examples:
- Recommend irrigation under vegetation stress
- Warn against pesticide application during high winds

### Streamlit Dashboard

- **Real-time Sensor Simulation**: Generates randomized but realistic data streams
- **Forecast Visualizations**: Line plots comparing actual vs predicted NDVI and wind
- **Adaptation Alerts**: Instant decision support messages based on conditions

## Repository Structure

## Repository Structure

climate_vegetation_dynamics/
├── climate_model.py              # Complete ML forecasting pipeline  
├── streamlit_app/  
│   ├── dashboard.py              # Streamlit frontend interface  
│   └── assets/                   # Forecast visuals, plots  
├── outputs/                      # Forecast results (CSVs, plots, metrics)  
├── data/                         # Sample input datasets  
├── requirements.txt              # Python dependencies  
├── .gitignore                    # Files/folders excluded from version control  
├── LICENSE                       # MIT License (optional)  
└── README.md                     # Project overview and documentation


## Getting Started

### Install Dependencies

pip install -r requirements.txt
streamlit run streamlit_app/dashboard.py
python climate_model.py

## Dependencies

- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- streamlit


## Demo

![Dashboard Preview](streamlit_app/assets/dashboard_preview.png)
