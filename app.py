from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
@app.route('/home')
def hello():
    return render_template("index.html")


@app.route('/predict',methods=['GET','POST'])

def send():
    if request.method=='POST':
       float_features=[float(x) for x in request.form.values()]
       final=[np.array(float_features)]
       print(float_features)
       print(final)
       prediction=model.predict(final)
       output = str(prediction[0])
       print(output)
       
       if output == 'Smelt':
           return render_template('smelt.html')
       elif output == 'Bream':
           return render_template('bream.html')
       elif output == 'Parkki':
           return render_template('parkki.html')
       elif output == 'Perch':
           return render_template('perch.html') 
       elif output == 'Pike':
           return render_template('pike.html')
       elif output == 'Roach':
           return render_template('roach.html')
       elif output == 'Whitefish':
           return render_template('whitefish.html')                       

       return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
