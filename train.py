""" produce an SVM to predict iris type """

import pickle
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

iris = datasets.load_iris()
iris_model = Pipeline(steps=[("scaler", StandardScaler()), ("svc", SVC())])
iris_model.fit(iris.data, iris.target)

with open("iris_model.pkl", "wb") as f:
    pickle.dump(iris_model, f)
