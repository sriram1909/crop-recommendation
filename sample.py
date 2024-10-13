import pickle

# car = ['suj', 'amberballa', 'arru']
#
# my_file = 'carpickle.pkl'
#
# fileobj = open(my_file, 'wb')
#
# pickle.dump(car, fileobj)

file = 'carpickle.pkl'

file_obj = open(file, 'rb')

car = pickle.load(file_obj)
print(car)

