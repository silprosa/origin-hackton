import joblib
model = joblib.load('ray.joblib')
import numpy as np
see =[99,3,3,4,5,3,4,2,4,34,20]
print(len(see))
pred= model.predict(np.array(see))