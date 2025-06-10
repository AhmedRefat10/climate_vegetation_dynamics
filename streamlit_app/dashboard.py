import streamlit as st
import pandas as pd
import numpy as np
import datetime
import random
import time
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="🌱 GreenX Dashboard", layout="wide")
st.title("🌿 The Green Flags - Climate Dashboard")
st.markdown("Real-time simulation of environmental conditions and decision support.")

# --- MODE SWITCHER ---
mode = st.radio("Choose Data Mode", ["🔴 Real-time Sensor Simulation", "📈 Model Forecasts"])

# --- DECISION SYSTEM ---
def adaptation_advice(ndvi, rainfall, wind_speed):
    advice = []
    if ndvi < 0.3:
        advice.append("⚠️ Vegetation stress detected. Consider irrigation.")
    if rainfall < 2:
        advice.append("💧 Low rainfall. Monitor soil moisture.")
    if wind_speed > 12:
        advice.append("🌬️ High wind alert. Delay pesticide spraying.")
    if not advice:
        advice.append("✅ Conditions stable. No immediate action needed.")
    return advice

# --- REAL-TIME SENSOR SIMULATION ---
if mode == "🔴 Real-time Sensor Simulation":
    def get_sensor_data():
        return {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "NDVI": round(random.uniform(0.2, 0.9), 3),
            "Rainfall (mm)": round(random.uniform(0, 20), 2),
            "Wind Speed": round(random.uniform(0, 15), 2)
        }

    placeholder = st.empty()
    data_log = []

    for _ in range(30):
        row = get_sensor_data()
        data_log.append(row)
        df = pd.DataFrame(data_log).sort_values(by="timestamp", ascending=False)

        with placeholder.container():
            st.subheader("📊 Latest Sensor Data")
            st.dataframe(df.head(10), use_container_width=True)

            st.subheader("🧠 Adaptation Advice")
            advice = adaptation_advice(row["NDVI"], row["Rainfall (mm)"], row["Wind Speed"])
            for tip in advice:
                st.info(tip)

        time.sleep(1)

    st.success("✅ Simulation complete.")

# --- MODEL FORECASTS SECTION ---
elif mode == "📈 Model Forecasts":
    def plot_forecast(df, actual_col, pred_col, title):
        fig, ax = plt.subplots(figsize=(5.5, 2.5))  # Smaller plot
        ax.plot(df['Date'], df[actual_col], label='Actual', linewidth=2)
        ax.plot(df['Date'], df[pred_col], label='Predicted', linestyle='--')
        ax.set_xlabel("Date")
        ax.set_ylabel(actual_col)
        ax.set_title(title)
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        return fig

    def display_forecast_row(files, actual_col, pred_col):
        cols = st.columns(2)
        for i, file in enumerate(files):
            try:
                df = pd.read_csv(file)
                df['Date'] = pd.to_datetime(df['Date'])
                with cols[i % 2]:
                    st.markdown(f"**📄 {file}**")
                    st.dataframe(df.tail(5), use_container_width=True)
                    fig = plot_forecast(df, actual_col, pred_col, file)
                    st.pyplot(fig)
                    st.markdown("---")  # Add spacing under each forecast
            except Exception as e:
                with cols[i % 2]:
                    st.warning(f"⚠️ Could not load {file}: {e}")

    # --- NDVI Forecasts ---
    st.subheader("🌿 NDVI Forecasts")
    display_forecast_row([
        "NDVI_predictions_NDVI_t+1.csv",
        "NDVI_predictions_NDVI_t+7.csv"
    ], "Actual NDVI", "Predicted NDVI")

    st.markdown(" ")  # Small spacer

    display_forecast_row([
        "NDVI_predictions_NDVI_t+16.csv",
        "NDVI_predictions_NDVI_t+30.csv"
    ], "Actual NDVI", "Predicted NDVI")

    st.markdown("## ")  # Space between NDVI and performance

    # --- NDVI Performance ---
    st.subheader("📊 NDVI Model Performance Summary")
    try:
        ndvi_metrics = pd.read_csv("NDVI_forecast_metrics.csv")
        st.dataframe(ndvi_metrics)
    except:
        st.warning("NDVI model metrics not found.")

    st.markdown("## ")  # Extra space before wind

    # --- WIND Forecasts ---
    st.subheader("🌬️ Wind Forecasts")
    display_forecast_row([
        "Wind_WindSpeed_t+1_forecast.csv",
        "Wind_WindSpeed_t+3_forecast.csv"
    ], "Actual", "Predicted")

    st.markdown(" ")  # Small spacer

    display_forecast_row([
        "Wind_WindDir_t+1_forecast.csv",
        "Wind_WindDir_t+7_forecast.csv"
    ], "Actual", "Predicted")

    st.markdown("## ")  # Space before wind metrics

    # --- WIND Performance ---
    st.subheader("📊 Wind Model Performance Summary")
    try:
        wind_metrics = pd.read_csv("Wind_forecast_metrics.csv")
        st.dataframe(wind_metrics)
    except:
        st.warning("Wind model metrics not found.")
