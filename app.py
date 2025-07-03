from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the saved model once when the API starts
model = joblib.load('rf_heart_model.pkl')

@app.route('/')
def home():
    return "Welcome to Heart Disease Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from POST request
        data = request.get_json(force=True)

        # Convert JSON to DataFrame (expects feature names as keys)
        input_df = pd.DataFrame([data])

        # Predict using the loaded model
        prediction = model.predict(input_df)[0]

        # Return prediction as JSON
        return jsonify({'heart_disease_prediction': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
