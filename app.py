from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('models/XGBoost.pkl', 'rb'))

# Define the crop dictionary
crop_indices = {
    "Soyabeans": 0,
    "Apple": 1,
    "Banana": 2,
    "Beans": 3,
    "Coffee": 4,
    "Cotton": 5,
    "Cowpeas": 6,
    "Grapes": 7,
    "Groundnuts": 8,
    "Maize": 9,
    "Mango": 10,
    "Orange": 11,
    "Peas": 12,
    "Rice": 13,
    "Watermelon": 14
}

# Create Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    # Collect input values from the form
    N = int(request.form.get('Nitrogen', 0))
    P = int(request.form.get('Phosporus', 0))
    K = int(request.form.get('Potassium', 0))
    ph = float(request.form.get('pH', 0.0))
    rainfall = float(request.form.get('Rainfall', 0.0))
    temperature = float(request.form.get('Temperature', 0.0))
    humidity = float(request.form.get('Humidity', 0.0))

    # Create feature vector
    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    # Make prediction using the model
    prediction_index = model.predict(data)[0]

    # Get the corresponding crop name from the dictionary
    predicted_crop = next((crop for crop, index in crop_indices.items() if index == prediction_index), "Unknown")

    # Return the predicted crop name to the template
    return render_template('index.html', result=predicted_crop)

if __name__ == "__main__":
    app.run(debug=True)
