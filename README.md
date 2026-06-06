# Crop Recommendation System

## Overview
The Crop Recommendation System is a machine learning-based web application that predicts the most suitable crop based on soil and environmental parameters. It integrates a trained machine learning model with a Flask web framework to provide real-time predictions through a web interface.

---

## Tech Stack

**Backend:**
- Python
- Flask

**Machine Learning:**
- Scikit-learn

**Frontend:**
- HTML5
- CSS3
- Bootstrap
- JavaScript

---

## How It Works
1. User enters soil and environmental parameters (N, P, K, temperature, humidity, pH, rainfall)  
2. Input data is processed and scaled using trained scaler models  
3. Machine learning model predicts the most suitable crop  
4. The result is displayed on the web interface  

---

## Project Structure
Crop-Recommendation-System/
├── app.py
├── model.pkl
├── MinMaxScaler.pkl
├── StandardScaler.pkl
├── requirements.txt
├── templates/
│ └── index.html
├── static/
│ ├── style.css
│ └── script.js
└── README.md

---

## How to Run
```bash
git clone https://github.com/your-username/Crop-Recommendation-System.git
cd Crop-Recommendation-System
pip install -r requirements.txt
python app.py

---

## Open in Browser
http://127.0.0.1:5000

---

## Note
This project was developed as a final year Computer Science project for academic and learning purposes
