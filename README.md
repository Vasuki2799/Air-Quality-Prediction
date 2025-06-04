# 🌍 Air Quality Prediction using Facebook Prophet



A Streamlit web app to forecast Air Quality Index (AQI) trends using the Facebook Prophet time series model. Upload your own CSV data and visualize trends, seasonality, and future AQI patterns.

## 📌 Table of Contents

🔍 Overview

🛠 Features

📁 Project Structure

▶️ Run the App

📷 Screenshots

📈 Future Work

## 🔍 Overview
Air quality is a growing concern in many parts of the world. This project uses Facebook Prophet to analyze historical AQI data and forecast future trends. It provides an interactive interface to upload data, visualize AQI distribution, and inspect forecast components.

## 🛠 Features

📂 Upload CSV files with date and aqi columns

🔮 Forecast AQI values for the next 30 days

📊 Visualize:
   * AQI over time
   * Average AQI by city (if available)
   * Prophet's forecast output
   * Trend, seasonality, and holidays

🎨 Beautiful UI with custom background

## 📁 Project Structure

├── air_quality.py               # Main Streamlit app

├── sample_data.csv              # Example input file

├── background.jpg               # Custom background image

├── README.md                    # Project description

└── requirements.txt             # Python dependencies

## ▶️ Run the App

# 🖥 Prerequisites
  * Python 3.8+
  * pip or conda
  * prophet, streamlit, pandas, matplotlib

# ⚙️ Installation

git clone https://github.com/Vasuki2799/air-quality-forecast-app.git

cd air-quality-forecast-app

pip install -r requirements.txt

# 🚀 Launch the app
streamlit run air_quality.py

# 📷 Screenshots
Home Page	Forecast View	Forecast Components
<img width="1440" alt="Screenshot 2025-06-04 at 11 29 16 AM" src="https://github.com/user-attachments/assets/42a37feb-35f5-49e5-a9ef-9aabdbbb08d9" />


# 📈 Future Work

* Include additional parameters like temperature, humidity, wind speed
* Integrate deep learning models (LSTM, GRU) for comparison
* Deploy on cloud (e.g., Streamlit Cloud or Heroku)
* Add login-based city-specific dashboards

## 🙋‍♂️ About Me

I'm a passionate data science enthusiast focused on building impactful machine learning applications.  
Feel free to connect and collaborate!

**Name:** Vasuki A 

**Email:** vasukiarul27@gmail.com  

**LinkedIn:** [linkedin.com/in/vasuki-arul](https://linkedin.com/in/vasuki-arul)  



# 📄 License

This project is licensed under the MIT License – see the LICENSE file for details.

