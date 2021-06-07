# Required Libraries
from flask import Flask, render_template, request, make_response
import jsonify
import requests
import json
from requests.sessions import Request
import pickle
import numpy as np


# Importing the model
#model = pickle.load(open('model.pkl','rb'))


app = Flask(__name__)


# Templates
# Home page
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/to_model", methods=['POST'])
def to_model():

    req = request.get_json()
    array = req['matrix_val']

    model_array = [3,3,3,3,3,3,3,3,3]
    
    for i in range(len(array)):
        if array[i]=='x':
            model_array[i]=1
        elif array[i]=='o':
            model_array[i]=2
    
    input_array = np.array(model_array)
    #prediction = model.predict([input_array])

    prediction = [1,0]

    output=prediction[0]

    blanks = model_array.count(3)
    outs = ""

    if blanks>=8:
        outs="WAIT"
    elif blanks==0:
        outs="OVER"
    elif output==0:
        outs="O"
    elif output==1:
        outs="X"

    x = {"output": outs}
    y = json.dumps(x)

    return y



if __name__=="__main__":
    app.run()

