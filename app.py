from flask import Flask, request, render_template
import numpy as np
import pickle
import os
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

# Sahi rasta (Path) dhoondne ke liye
base_dir = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(os.path.join(base_dir, 'model.pkl'), 'rb'))
sc = pickle.load(open(os.path.join(base_dir, 'standscaler.pkl'), 'rb'))
ms = pickle.load(open(os.path.join(base_dir, 'minmaxscaler.pkl'), 'rb'))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/crop-info')
def crop_info():
    return render_template("crop-information.html")

@app.route("/predict", methods=['POST'])
def predict():
    try:
        feature_list = [
            float(request.form['Nitrogen']),
            float(request.form['Phosporus']),
            float(request.form['Potassium']),
            float(request.form['Temperature']),
            float(request.form['Humidity']),
            float(request.form['Ph']),
            float(request.form['Rainfall'])
        ]
        single_pred = np.array(feature_list).reshape(1, -1)
        scaled_features = ms.transform(single_pred)
        final_features = sc.transform(scaled_features)
        prediction = model.predict(final_features)

        crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

        if prediction[0] in crop_dict:
            result = f"{crop_dict[prediction[0]]} is the best crop for this soil."
        else:
            result = "Could not determine the crop."
        return render_template('index.html', result=result)
    except:
        return render_template('index.html', result="Error: Please enter valid numbers.")

if __name__ == "__main__":
    app.run(debug=True)