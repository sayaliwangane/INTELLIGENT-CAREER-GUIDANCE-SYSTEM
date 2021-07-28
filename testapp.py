from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


@app.route('/')
def career():
    return render_template("hometest.html")


@app.route('/predict',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      i = 0
      print(result)
      res = result.to_dict(flat=True)
      print("res:",res)
      arr1 = res.values()
      arr = ([value for value in arr1])

      data = np.array(arr)

      data = data.reshape(1,-1)
      print(data)
      loaded_model = pickle.load(open("careerlast.pkl", 'rb'))
      predictions = loaded_model.predict(data)
     # return render_template('testafter.html',a=predictions)
      
      print(predictions)
      pred = loaded_model.predict_proba(data)
      print(pred)
      #acc=accuracy_score(pred,)
      pred = pred > 0.05
      #print(predictions)
      i = 0
      j = 0
      index = 0
      res = {}
      final_res = {}
      while j < 17:
          if pred[i, j]:
              res[index] = j
              index += 1
          j += 1
      # print(j)
      #print(res)
      index = 0
      for key, values in res.items():
          if values != predictions[0]:
              final_res[index] = values
              print('final_res[index]:',final_res[index])
              index += 1
      #print(final_res)
      jobs_dict = {0:'AI ML Specialist',
                   1:'API Integration Specialist',
                   2:'Application Support Engineer',
                   3:'Business Analyst',
                   4:'Customer Service Executive',
                   5:'Cyber Security Specialist',
                   6:'Data Scientist',
                   7:'Database Administrator',
                   8:'Graphics Designer',
                   9:'Hardware Engineer',
                   10:'Helpdesk Engineer',
                   11:'Information Security Specialist',
                   12:'Networking Engineer',
                   13:'Project Manager',
                   14:'Software Developer',
                   15:'Software Tester',
                   16:'Technical Writer'}
                
      #print(jobs_dict[predictions[0]])
      job = {}
      #job[0] = jobs_dict[predictions[0]]
      index = 1
     
        
      data1=predictions[0]
      print(data1)
      return render_template("testafter.html",final_res=final_res,job_dict=jobs_dict,job0=data1)
      
if __name__ == '__main__':
   app.run(debug = True)
