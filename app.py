# Importing necessary libraries
from flask import Flask, render_template, request
from joblib import load

# Creating a Flask app instance
app = Flask(__name__)

# Loading the pre-trained model
model = load('Online_payment_fraud_detection.pkl')

# Route for the home page where users can input data
@app.route('/')
def predictor():
    return render_template('index.html')

# Route to handle the form submission and display the result
@app.route('/result', methods=['GET'])
def forminfo():
    # Extracting data from the form
    step = int(request.args.get('step'))
    type = int(request.args.get('type'))
    amount = float(request.args.get('amount'))
    nameOrig = str(request.args.get('nameOrig'))
    oldbalanceOrg = float(request.args.get('oldbalanceOrg'))
    nameDest = str(request.args.get('nameDest'))
    newbalanceOrig = float(request.args.get('newbalanceOrig'))
    oldbalanceDest = float(request.args.get('oldbalanceDest'))
    newbalanceDest = float(request.args.get('newbalanceDest'))
    isFlaggedFraud = int(request.args.get('isFlaggedFraud'))

    # Making the prediction using the loaded model
    y_pred = model.predict([[step, type, amount, nameOrig, oldbalanceOrg, nameDest, newbalanceOrig, oldbalanceDest, newbalanceDest, isFlaggedFraud]])

    # Converting the prediction to human-readable text
    if y_pred[0] == 1:
        result = 'Fraud'
    else:
        result = 'Not Fraud'

    # Rendering the result template with the prediction
    return render_template('result.html', result=result)

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)
