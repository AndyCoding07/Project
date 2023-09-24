from django.shortcuts import render
import pandas as pd
from sklearn.linear_model import LogisticRegression

def index(request):
    return render(request, "index.html")


def predictpage(request):
    return render(request, "predictpage.html")


def result(request):
    # creating dataframe 
    dataframe = pd.read_csv("F:\BSC CS\semister 5\PROJECT SEM 5\diabetes.csv")

    # X contains indenpendent variables Y is dependent variable 
    X = dataframe.drop("Outcome", axis=1)
    Y = dataframe["Outcome"]

    # if you want to find accuracy of model 
    # X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    # training model 
    model = LogisticRegression()
    model.fit(X, Y)

    # saving user input into variables 
    preg = float(request.GET['preg'])
    glucose = float(request.GET['glucose'])
    bp = float(request.GET['bp'])
    skin = float(request.GET['skin'])
    insulin = float(request.GET['insulin'])
    bmi = float(request.GET['bmi'])
    dpf = float(request.GET['dpf'])
    age = float(request.GET['age'])

    # predicting outcome based on users input 
    prediction = model.predict([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])

    if (prediction == [1]):
        result = "POSITIVE for Diabetes."
    else:
        result = "NEGATIVE for Diabetes."

    return render(request, "predictpage.html", {"result": result})