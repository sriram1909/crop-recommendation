import pickle

file = 'carpickle.pkl'

file_obj = open(file, 'rb')

car = pickle.load(file_obj)
print(car)

