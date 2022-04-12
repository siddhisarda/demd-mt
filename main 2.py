from flask import Flask, request
from flasgger import Swagger
import pickle
from sklearn.linear_model import LogisticRegression

app = Flask(_name_)
Swagger(app)

pickled_model = open("pickle_diabetes_model.pkl","rb")
classifier = pickle.load(pickled_model)

@app.route('/')  #decorators
def home():
    return "Diabetes predictor"

@app.route('/predict')
def predict_diabetes():

    """Lets try Swagger from flasgger
    ---
    parameters:
        - name: age
          in: query
          type: number
          required: true  
        - name: sex
          in: query
          type: number
          required: true
        - name: bmi
          in: query
          type: number
          required: true
        - name: bp
          in: query
          type: number
          required: true
        - name: s1
          in: query
          type: number
          required: true
        - name: s2
          in: query
          type: number
          required: true
        - name: s3
          in: query
          type: number
          required: true
        - name: s4
          in: query
          type: number
          required: true
        - name: s5
          in: query
          type: number
          required: true
        - name: s6
          in: query
          type: number
          required: true


    responses:
        200:
            description: The result is    
    """

    a1 = request.args.get("age")
    a2 = request.args.get("sex")
    a3 = request.args.get("bmi")
    a4 = request.args.get("s1")
    a5 = request.args.get("s2")
    a6 = request.args.get("s3")
    a7 = request.args.get("s4")
    a8 = request.args.get("s5")
    a9 = request.args.get("s6")

    result = classifier.predict([[a1,a2,a3,a4,a5,a6,a7,a8,a9]])

    return f"The flower prediction is{result}"

if _name_ == "_main_":
    app.run()