# app/main.py
from flask import Flask, request, jsonify
import pickle
import pandas as pd
from scoring_script import score_function  # Assuming your scoring logic is in scoring_script.py

app = Flask(__name__)

# Define your API token
API_TOKEN = '12345'

# Load the model
with open('app/model.pkl', 'rb') as f:
    model = pickle.load(f)

def check_token(request):
    token = request.headers.get('Authorization')
    if token == API_TOKEN:
        return True
    else:
        return False

@app.route('/predict', methods=['POST'])
def predict():
    if not check_token(request):
        return jsonify({'error': 'Unauthorized access'}), 401

    try:
        data = request.get_json(force=True)
        # Assuming the input data is in a format suitable for your model
        df = pd.DataFrame([data])
        prediction = score_function(model, df)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
