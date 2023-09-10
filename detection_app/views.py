from django.shortcuts import render
from joblib import load

model= load('savedModels/Online payment fraud detection(capstone)-Copy1.joblib')


def predictor(request):
    return render(request,'index.html')

def forminfo(request):
    step = int(request.GET['step'])
    type = int(request.GET['type'])
    amount = float(request.GET['amount'])
    nameOrig=float(request.GET['nameOrig']) 
    oldbalanceOrg = float(request.GET['oldbalanceOrg'])
    nameDest=int(request.GET['nameDest'])
    newbalanceOrig = float(request.GET['newbalanceOrig'])
    isFlaggedFraud = int(request.GET['isFlaggedFraud'])
    y_pred = model.predict([[step,type,amount,nameOrig,oldbalanceOrg,nameDest,newbalanceOrig,isFlaggedFraud]])
    if y_pred[0] == 1:
        y_pred = 'Fraudulent Transaction'
    else :
        y_pred = 'Not Fraudulent Transaction'
    return render(request,'result.html',{'result':y_pred})