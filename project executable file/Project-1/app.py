from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import pickle
app=Flask(__name__)
model=pickle.load(open('temp.pkl','rb'))
app=Flask(__name__,template_folder='template')
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
   input_feature=[x for x in request.form.values()]
   input_feature=np.transpose(input_feature)
   input_feature=[np.array(input_feature)]
   print(input_feature)
   names=['CO2_room', 'Relative_humidity_room', 'Lighting_room', 'Meteo_Rain',
       'Meteo_Wind', 'Meteo_Sun_light_in_west_facade',
       'Outdoor_relative_humidity_Sensor']
   data=pd.DataFrame(input_feature,columns=names)
   prediction=model.predict(data)
   result=int(prediction[0])
   print(result)
   return render_template('result.html', prediction_text='your room temparture will be {}'.format(result))
if __name__=='__main__':
    app.run()
