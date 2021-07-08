import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template
from enum import Enum

app=Flask(__name__)  
pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

class Species(Enum):
 Bream = 0
 Roach = 1
 Whitefish = 2
 Parkki = 3
 Perch = 4
 Pike = 5
 Smelt = 6

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = list(map(float, [x for x in request.form.values()]))
    
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)
    predict = Species(prediction[0])
    print(Species(prediction[0]))
    return render_template('index.html', prediction_text='The fish belong to {} '. format(Species(prediction[0])))

if __name__=='__main__':
    app.run()