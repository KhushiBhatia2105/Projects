from flask import Flask, render_template,request
import pickle
import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()


logmodel =pickle.load(open('iris_classifier_knn.pkl','rb'))


app = Flask(__name__)
 
@app.route('/')
def login():
    return render_template('index.html')



@app.route('/prediction', methods=['POST'])
def prediction():
    data = [float(x) for x in request.form.values()]
    print(data)
    preds = logmodel.predict([data])
    pred_species = [iris.target_names[p] for p in preds]
    print(pred_species)
    
    return render_template('index.html',prediction_text = 'your output is {}'.format(pred_species))



if __name__ == '__main__':
   app.run(debug=True)