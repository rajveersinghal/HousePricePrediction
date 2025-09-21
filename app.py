import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy

app= Flask(__name__)



data = pd.read_csv("C:\\Users\\avipa\\OneDrive\\Desktop\\Live project 1\\HousePricePrediction\\datasets\\Cleaned_Data.csv")
pipe = pickle.load(open("C:\\Users\\avipa\\OneDrive\\Desktop\\Live project 1\\HousePricePrediction\\model\\RidgeModel.pkl", 'rb'))

@app.route('/')
def index():
    locations = sorted(data['location'].unique()) 
    return render_template('index.html', locations=locations) 


@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('sqft')

    print(location, bhk, bath, sqft)  # Debugging purpose

    # Convert input data to appropriate types
    try:
        bhk = int(bhk)
        bath = int(bath)
        sqft = float(sqft)
    except ValueError:
        return "Invalid input. Please enter numeric values for BHK, Bath, and Square Feet.", 400

    # Make a prediction using the model
    input_data = pd.DataFrame([[location, sqft, bath, bhk]], 
                              columns=['location', 'total_sqft', 'bath', 'bhk'])
    predicted_price = pipe.predict(input_data)[0] * 1e5
    if predicted_price >= 1e7:
        price_str = f" {predicted_price/1e7:.2f} Cr"
    else:
        price_str = f" {predicted_price/1e5:.2f} Lakh"

    return price_str

if __name__ == '__main__':
    app.run(debug=True, port=5000)
