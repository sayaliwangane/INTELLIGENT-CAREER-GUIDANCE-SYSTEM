from sklearn import model_selection
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
import pickle
  
# load the data
dataset = pd.read_csv('dataset9000.data', header = None)
print(dataset.head())
X=np.array(dataset.iloc[:, 0:17]) 
print(X)
Y = np.array(dataset.iloc[:, 17])
print(Y)
dataset.columns= ["Database Fundamentals","Computer Architecture","Distributed Computing Systems",
"Cyber-Security","Networking","Development","Programming Skills","Project Management",
"Computer Forensics Fundamentals","Technical Communication","AI ML","Software Engineering","Business Analysis",
"Communication skills","Data Science","Troubleshooting-skills","Graphics Designing","Roles"]
dataset.dropna(how ='all', inplace = True)

  
seed =5 
kfold = model_selection.KFold(n_splits = 15,
                       random_state = seed)
  
# initialize the base classifier
base_cls = DecisionTreeClassifier()
  
# no. of base classifier
num_trees = 50
  
# bagging classifier
model = BaggingClassifier(base_estimator = base_cls,
                          n_estimators = num_trees,
                          random_state = seed)
  
results = model_selection.cross_val_score(model, X, Y, cv = kfold)
print("accuracy :",results.mean()*100)


