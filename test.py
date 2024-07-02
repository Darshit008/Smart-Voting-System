import pickle

f = open('data/names.pkl',"rb")
l = pickle.load(f)
print(l)