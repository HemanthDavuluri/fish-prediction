import pandas as pd 
import pickle

data = pd.read_csv('Fish.csv')


#print(data.head())

from sklearn.linear_model import *
from sklearn.model_selection import train_test_split

X = data.drop(columns=['Species'])
y = data.Species

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()

model.fit(X_train,y_train)

pickle.dump(model,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))
