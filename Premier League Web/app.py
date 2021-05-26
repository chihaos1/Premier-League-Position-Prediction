import numpy as np
import math
from flask import Flask, render_template, request
import pickle  

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('prediction.html')

@app.route('/prediction', methods=['GET','POST'])
def prediction():
    int_feat = [int(x) for x in request.form.values()]
    deficit = int_feat[4] - int_feat[5]
    points = 3 * int_feat[1] + 1 * int_feat[2]
    int_feat.extend([deficit, points])
    
    final_feat = [np.array(int_feat)]
    prediction = model.predict(final_feat)
    
    output = math.ceil(prediction)
    
    return render_template('prediction.html', 
                           prediction_text="Team's Predicted Position: {}".format(output))
    
if __name__ == '__main__':
    app.run(debug=True)