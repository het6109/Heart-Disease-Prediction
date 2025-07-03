# Heart Disease Prediction and Health Monitoring System

## Project Overview

This project demonstrates an end-to-end machine learning pipeline for predicting heart disease risk using clinical data. It includes:

- Data exploration, preprocessing, and visualization in a Jupyter Notebook
- Training and evaluation of machine learning models (Logistic Regression and Random Forest)
- Deployment of the trained model as a REST API using Flask for real-time predictions

The goal is to build a complete health monitoring system from scratch, showcasing both data science and deployment skills.

---

## Features

- Exploratory Data Analysis (EDA) with visualizations
- Data preprocessing with scaling and one-hot encoding
- Model training using scikit-learn pipelines
- Model evaluation with classification reports, confusion matrices, and ROC curves
- Flask API serving the trained model for prediction on new data

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. Clone the repository:
   git clone https://github.com/het6109/Heart-Disease-Prediction.git
   cd Heart-Disease-Prediction

2. (Recommended) Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install required packages:
   pip install -r requirements.txt


---

## Usage

### 1. Jupyter Notebook

- Open and run the notebook `Heart_Disease_Prediction.ipynb` to explore data, train, and evaluate models.


### 2. Running the Flask API

- Make sure the trained model file (`rf_heart_model.pkl`) is in the project directory.
- Run the Flask app:

python app.py


- The API will be available at `http://127.0.0.1:5000/`

### 3. Making Predictions

Send a POST request to `/predict` endpoint with JSON data containing patient features. Example using `curl`:

curl -X POST -H "Content-Type: application/json" -d '{
"Age": 63,
"Sex": "M",
"ChestPainType": "ATA",
"RestingBP": 145,
"Cholesterol": 233,
"FastingBS": 1,
"RestingECG": "Normal",
"MaxHR": 150,
"ExerciseAngina": "N",
"Oldpeak": 2.3,
"ST_Slope": "Up"
}' http://127.0.0.1:5000/predict


---

## Project Structure

├── Heart_Disease_Prediction.ipynb # Jupyter notebook with full ML workflow
├── app.py # Flask API script
├── rf_heart_model.pkl # Saved Random Forest model pipeline
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---





