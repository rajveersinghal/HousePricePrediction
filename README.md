# House Price Prediction using Machine Learning

This project predicts house prices in Bangalore based on features like location, total square feet, number of bedrooms (BHK), and number of bathrooms. The model is built using machine learning, and the user interface is developed using HTML, CSS, and Flask.

## Features
- Predict house prices based on input parameters
- Interactive UI built with HTML, CSS, and Flask
- Uses a machine learning model trained on a Bangalore housing dataset

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Deployment**: Flask

## Dataset
The dataset used for training the model contains information on Bangalore house prices with features such as:
- **Location**
- **Total square feet**
- **BHK (Bedrooms, Hall, Kitchen)**
- **Number of bathrooms**

## Installation & Setup
Follow these steps to set up and run the project locally:

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the Application
```sh
python app.py
```

### 5. Access the Web App
Once the server starts, open your browser and go to:
```
http://127.0.0.1:5000/
```

## Model Training
To train the model from scratch:
1. Load the dataset.
2. Preprocess the data (handle missing values, encode categorical variables, feature scaling).
3. Train a machine learning model (e.g., Linear Regression, Decision Tree, or Random Forest).
4. Save the trained model using  `pickle`.

## Project Structure
```
├── static/              # CSS, JS, images
├── templates/           # HTML templates
├── app.py               # Flask application
├── model.py             # ML model training and prediction
├── requirements.txt     # Dependencies
├── README.md            # Project documentation
```

## Screenshots
![Image](https://github.com/user-attachments/assets/4e47fcf5-1025-4104-a978-5848b2929ea5)



## Future Enhancements
- Improve UI with Bootstrap
- Add more features for prediction (e.g., amenities, locality insights)
- Deploy on a cloud platform (AWS, Heroku, etc.)

## License
This project is licensed under the MIT License.

---

Feel free to contribute to this project by submitting issues and pull requests!

Render Link 
https://housepriceprediction-2-l6dm.onrender.com/
