from flask import Flask, render_template,request
import pandas as pd
app = Flask(__name__)
import pickle
import joblib
model = pickle.load(open("svd.pkl",'rb'))



@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/guest', methods =["post"])
def Guest():
    pc0 = request.form["pc0"]
    pc1 = request.form["pc1"]
    pc2 = request.form["pc2"]
    data =[[pc0,pc1,pc2]]
    data1= pd.DataFrame(data,columns=['pc0','pc1','pc2'])
    #prediction = model.fit_transform((data1))
    prediction=model.predict(data1)
    return render_template("index.html",y = prediction)

if __name__=='__main__':
    app.run(debug = True)



                           #@app.route('/user')
#def user ():
   # return "hellow user welcome"
