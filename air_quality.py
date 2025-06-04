import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
from streamlit_option_menu import option_menu
import seaborn as sns

# Customizing the page layout and background
st.set_page_config(page_title="Air Quality Prediction", layout="wide")

import base64

def set_background_image(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()

    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #1f2937;
    }}
    [data-testid="stSidebar"] {{
        background: rgba(255, 255, 255, 0.9);
    }}
    h1, h2, h3, h4 {{
        color: #2c3e50;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# 🔽 Call this early in your script
set_background_image("Screenshot 2025-06-04 at 10.48.30 AM.png")


# Sidebar with navigation menu
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Forecast", "Forecast Components", "About"],
        icons=["house", "bar-chart", "database", "info-circle"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#FFD700"},
            "icon": {"color": "#333", "font-size": "20px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin": "5px", "color": "#333"},
            "nav-link-selected": {"background": "#D2B48C", "color": "Chocolate", "font-weight": "bold"},
        },
    )


# Home Page
if selected == "Home":
    st.markdown("<h1 style='color: #FF4500;'>AIR QUALITY PREDICTION USING PROPHET</h1>", unsafe_allow_html=True)
    st.markdown("""
    Welcome to the **Air Quality Prediction App**! 🌱  
    This application uses **Facebook Prophet**, a powerful time series forecasting tool, to predict future **Air Quality Index (AQI)** values based on historical pollution data.""")

    st.markdown("<h2 style='color: #B22222	;'>🔍 Key Features</h2>", unsafe_allow_html=True)
    ("""
    - 📈 Forecast AQI levels with Prophet
    - 📊 Visualize trends, seasonality, and future patterns
    - 💡 Upload your custom CSV data
    
    Use the sidebar to explore the forecasting and components.
    """)

   # Space for Video
    st.subheader("📽️ Video")
    video_path = "/Users/arul/Documents/VASUKI/projects/Screen Recording 2025-06-04 at 11.14.36 AM.mov"  # Replace with your video file
    st.video(video_path)


# Forecast
elif selected == "Forecast":
    st.markdown("<h1 style='color: #FF4500;'>AQI Forecast</h1>", unsafe_allow_html=True)
    st.markdown("Upload your CSV data to generate forecasts for the AQI using Prophet.")

    # Sample CSV download
    sample_data = """date,aqi
2024-01-01,120
2024-01-02,130
2024-01-03,128
2024-01-04,125
2024-01-05,135
"""
    st.download_button(
        label="📥 Download Sample CSV",
        data=sample_data,
        file_name='sample_aqi_data.csv',
        mime='text/csv'
    )

    # 🔽 You can plug in your file uploader and forecasting logic below here
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("📄 Data Preview")
        st.dataframe(df.head())

        # ✅ Input validation
        required_cols = {'date', 'aqi'}
        if not required_cols.issubset(df.columns):
            st.error("❌ Your CSV must contain at least 'date' and 'aqi' columns.")
        else:
            # 🧼 Clean and format date
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            df.dropna(subset=['date', 'aqi'], inplace=True)

            # 📊 Extra Visualization: AQI by City
            if 'city' in df.columns:
                st.subheader("📍 Average AQI by City")
                city_avg = df.groupby('city')['aqi'].mean().sort_values(ascending=False)
                st.bar_chart(city_avg)

            # 📈 Extra Visualization: AQI over Time
            df.set_index('date', inplace=True)
            daily_avg = df['aqi'].resample('D').mean()
            st.subheader("📅 Daily AQI Trend")
            st.line_chart(daily_avg)
            df.reset_index(inplace=True)  # reset for Prophet

            # 📅 Prepare data for Prophet
            prophet_df = df[['date', 'aqi']].rename(columns={'date': 'ds', 'aqi': 'y'})

            # 🔮 Forecasting
            model = Prophet()
            model.fit(prophet_df)

            future = model.make_future_dataframe(periods=30)
            forecast = model.predict(future)

            st.subheader("📊 Forecast Output (Next 30 Days)")
            st.write(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

            fig1 = model.plot(forecast)
            st.pyplot(fig1)

            # ⛳ Save forecast to session state for use in other tabs
            st.session_state['forecast'] = forecast
            st.session_state['model'] = model
    else:
        st.info("📂 Please upload a CSV file to proceed.")

# Forecast Components
elif selected == "Forecast Components":
    st.markdown("<h1 style='color: #FF4500;'>Forecast Components</h1>", unsafe_allow_html=True)
    st.markdown("Decompose the forecast into **trend**, **weekly**, and **yearly** seasonality.")

    if 'forecast' in st.session_state and 'model' in st.session_state:
        try:
            fig2 = st.session_state.model.plot_components(st.session_state.forecast)
            st.pyplot(fig2)
        except Exception as e:
            st.error(f"❌ Could not generate forecast components: {e}")
    else:
        st.warning("⚠️ Please generate a forecast first from the Forecast tab.")

# About
elif selected == "About":
    st.markdown("<h1 style='color: #FF4500;'>About This Project</h1>", unsafe_allow_html=True)
    st.markdown("""
    This project is designed to **predict air quality trends** using time series forecasting.""")

    st.markdown("<h2 style='color: #B22222	;'>Advantages</h2>", unsafe_allow_html=True)
    ("""
    - Handles missing data and outliers
    - Captures trends, seasonality, and anomalies
    - Flexible and scalable for multiple cities""")

    st.markdown("<h2 style='color: #B22222	;'>Tools Used</h2>", unsafe_allow_html=True)
    ("""
    - `Streamlit` for frontend
    - `Facebook Prophet` for forecasting
    - `Pandas` and `Matplotlib` for data handling and visualization""")

    st.markdown("<h2 style='color: #B22222	;'>Feature Enahancemet</h2>", unsafe_allow_html=True)
    ("""
    - Include weather parameters (temperature, humidity, wind speed)
    - Deploy as a web app for real-time predictions
    - Compare Prophet with LSTM/GRU models
    """)
