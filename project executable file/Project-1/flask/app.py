from flask import Flask,request,render_template
import pickle
import numpy as np
import pandas as pd

app=Flask('__name__')

model = pickle.load(open("model.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict')
def innerpage():
    return render_template("inner-page.html")

@app.route('/submit',methods=["POST","GET"])# route to show the predictions in a web UI
def submit():
    #  reading the inputs given by the user
    input_feature=[float(x) for x in request.form.values()]  
    #input_feature = np.transpose(input_feature)
    x=[np.array(input_feature)]
    print(input_feature)
    names =  ['Nausea/Vomting', 'ALT 1', 'RNA 12', 'ALT after 24 w', 'RNA EF',
    'RNA Base', 'Jaundice ', 'WBC',  'Fatigue & generalized bone ache ', 'Gender', 'RBC', 'HGB']
    data = pd.DataFrame(x,columns=names)
    print(data)
    pred = model.predict(data)
   
    if(pred == 0):
        return render_template("portfolio-details.html", predict = "No signs of Hepatitis detected. Stay healthy!")
    elif(pred == 1):
        return render_template("portfolio-details.html",predict = "Warning: Signs of Hepatitis detected.Consult a healthcare professional")
    else:
        return render_template("portfolio-details.html",predict = "Invalid prediction value. Please check your readings.")
    
    
    
if __name__ == "__main__":
    
    app.run(debug = False,port = 2020)