import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def inputPage():
    return render_template('Input.html')


def valuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,13)
    loaded_model = pickle.load(open("algo.pickle", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        prediction = valuePredictor(to_predict_list)
        return render_template('result.html', prediction=prediction)


app.run()
