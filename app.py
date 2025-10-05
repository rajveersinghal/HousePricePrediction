import pandas as pd
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# ------------------------
# Load Bengaluru dataset + model
# ------------------------
blr_data = pd.read_csv("C:\\Users\\avipa\\OneDrive\\Desktop\\Live project 1\\HousePricePrediction\\datasets\\Cleaned_Data.csv")
blr_model = pickle.load(open("C:\\Users\\avipa\\OneDrive\\Desktop\\Live project 1\\HousePricePrediction\\model\\RidgeModel.pkl", 'rb'))

# ------------------------
# Load Delhi dataset + model
# ------------------------
delhi_data = pd.read_csv("C:\\Users\\avipa\\OneDrive\\Desktop\\Live project 1\\HousePricePrediction\\datasets\\newdataset.csv")
delhi_model = pickle.load(open("C:\\Users\\avipa\\OneDrive\\Desktop\\Live project 1\\HousePricePrediction\\model\\RidgeModel_d.pkl", 'rb'))

# ------------------------
# Home route
# ------------------------
@app.route('/')
def index():
    cities = ["Bengaluru", "Delhi"]  # let user select the city
    locations = {
        "Bengaluru": sorted(blr_data['location'].unique()),
        "Delhi": sorted(delhi_data['location'].unique())
    }
    return render_template('index.html', cities=cities, locations=locations)

# ------------------------
# Prediction route
# ------------------------
@app.route('/predict', methods=['POST'])
def predict():
    city = request.form.get('city')        # user selects city
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('sqft')

    print(city, location, bhk, bath, sqft)  # Debugging

    # Convert numeric inputs
    try:
        bhk = int(bhk)
        bath = int(bath)
        sqft = float(sqft)
    except ValueError:
        return "Invalid input. Please enter numeric values for BHK, Bath, and Square Feet.", 400

    # Choose dataset + model depending on city
    if city == "Bengaluru":
        model = blr_model
    elif city == "Delhi":
        model = delhi_model
    else:
        return "Invalid city selected.", 400

    # Prepare input
    input_data = pd.DataFrame([[location, sqft, bath, bhk]],
                              columns=['location', 'total_sqft', 'bath', 'bhk'])

    # Predict
    predicted_price = model.predict(input_data)[0] * 1e5

    if predicted_price >= 1e7:
        price_str = f"{predicted_price/1e7:.2f} Cr"
    else:
        price_str = f"{predicted_price/1e5:.2f} Lakh"

    return price_str


if __name__ == '__main__':
    app.run(debug=True, port=5000)
