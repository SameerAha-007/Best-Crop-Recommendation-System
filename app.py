from flask import Flask, request, render_template, jsonify
import numpy as np
import joblib
from pymongo import MongoClient
from datetime import datetime  # for timestamp

# Load model and label encoder
model = joblib.load('xgboost_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://skshdjdhsj:BMFMmPbxHBW4e6jV@cluster.i9x2fg8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster")
db = client['crop_prediction_db']
collection = db['predictions']
# Define crop details and image URLs
crop_data = {
    'rice': {'details': 'Rice is a staple food.', 'image_url': '/static/images/rice.jpg'},
    'maize': {'details': 'Maize is used for food and feed.', 'image_url': '/static/images/maize.jpg'},
    'chickpea': {'details': 'Chickpeas are a protein-rich legume.', 'image_url': '/static/images/chickpea.jpg'},
    'kidneybeans': {'details': 'Kidney beans are popular in many dishes.', 'image_url': '/static/images/kidneybeans.jpg'},
    'pigeonpeas': {'details': 'Pigeon peas thrive in tropical climates.', 'image_url': '/static/images/pigeonpeas.jpg'},
    'mothbeans': {'details': 'Moth beans are drought-tolerant.', 'image_url': '/static/images/mothbeans.jpg'},
    'mungbean': {'details': 'Mung beans are commonly sprouted.', 'image_url': '/static/images/mungbean.jpg'},
    'blackgram': {'details': 'Black gram is used in many Indian dishes.', 'image_url': '/static/images/blackgram.jpg'},
    'lentil': {'details': 'Lentils are rich in protein.', 'image_url': '/static/images/lentil.jpg'},
    'pomegranate': {'details': 'Pomegranates are antioxidant-rich.', 'image_url': '/static/images/pomegranate.jpg'},
    'banana': {'details': 'Bananas are a great energy source.', 'image_url': '/static/images/banana.jpg'},
    'mango': {'details': 'Mangoes are the "king of fruits".', 'image_url': '/static/images/mango.jpg'},
    'grapes': {'details': 'Grapes are used for wine and juice.', 'image_url': '/static/images/grapes.jpg'},
    'watermelon': {'details': 'Watermelons are refreshing.', 'image_url': '/static/images/watermelon.jpg'},
    'muskmelon': {'details': 'Muskmelons are sweet and juicy.', 'image_url': '/static/images/muskmelon.jpg'},
    'apple': {'details': 'Apples are crisp and nutritious.', 'image_url': '/static/images/apple.jpg'},
    'orange': {'details': 'Oranges are rich in Vitamin C.', 'image_url': '/static/images/orange.jpg'},
    'papaya': {'details': 'Papayas are tropical fruits.', 'image_url': '/static/images/papaya.jpg'},
    'coconut': {'details': 'Coconuts provide oil and water.', 'image_url': '/static/images/coconut.jpg'},
    'cotton': {'details': 'Cotton is used for textiles.', 'image_url': '/static/images/cotton.jpg'},
    'Sapota': {'details': 'Sapota is a tropical fruit.', 'image_url': '/static/images/sapota.jpg'},
    'fingermillet': {'details': 'Finger millet is rich in calcium.', 'image_url': '/static/images/fingermillet.jpg'},
    'Carrots': {'details': 'Carrots are rich in beta-carotene.', 'image_url': '/static/images/carrots.jpg'},
    'Chili': {'details': 'Chilies add heat to dishes.', 'image_url': '/static/images/chili.jpg'},
    'Cinnamon': {'details': 'Cinnamon is a popular spice.', 'image_url': '/static/images/cinnamon.jpg'},
    'Corn': {'details': 'Corn is a versatile crop.', 'image_url': '/static/images/maize.jpg'},
    'Eggplant': {'details': 'Eggplants are used in many cuisines.', 'image_url': '/static/images/eggplant.jpg'},
    'Strawberries': {'details': 'Strawberries are sweet fruits.', 'image_url': '/static/images/strawberries.jpg'},
    'Sunflowers': {'details': 'Sunflowers provide seeds and oil.', 'image_url': '/static/images/sunflowers.jpg'},
    'Tomato': {'details': 'Tomatoes are used worldwide.', 'image_url': '/static/images/tomato.jpg'},
    'Wheat': {'details': 'Wheat is a staple cereal.', 'image_url': '/static/images/wheat.jpg'}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nav')
def nav():
    return render_template('nav.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])

        # Prepare input for model
        data = np.array([[N, P, K, temperature, humidity, ph]])

        # Make prediction
        prediction = model.predict(data)
        original_label = label_encoder.inverse_transform(prediction)[0]

        # Get crop info
        crop_info = crop_data.get(original_label, {
            'details': 'No details available.',
            'image_url': '/static/images/placeholder.jpg'
        })

        # Store in MongoDB
        collection.insert_one({
            "timestamp": datetime.utcnow(),
            "input": {
                "N": N, "P": P, "K": K,
                "temperature": temperature,
                "humidity": humidity,
                "ph": ph
            },
            "prediction": original_label
        })

        # Show result page
        return render_template(
            'result.html',
            prediction=original_label,
            details=crop_info['details'],
            image_url=crop_info['image_url']
        )

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)