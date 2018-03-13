import pandas as pd 
import numpy as np
from keras.utils.np_utils import to_categorical

def load_arabic_digit():
	return load_arabic_digits_helper(
		'dataset/arabic-digits/csvTrainImages.csv',
		'dataset/arabic-digits/csvTrainLabel.csv')

def load_arabic_digit_test():
	return load_arabic_digits_helper(
		'dataset/arabic-digits/csvTestImages.csv',
		'dataset/arabic-digits/csvTestLabel.csv')

def load_arabic_digits_helper(item_file,label_file):
	items = pd.read_csv(item_file,header=None).values
	labels = pd.read_csv(label_file,header=None).values
	
	# Shape hte ietms from a 10 vector into 28x28 2D vector
	items = items.reshape(items.shape[0],28,28)
	
	# Rotate image foe easy visualization
	items  = np.array([np.fliplr(np.rot90(d,k=3)) for d in items])
	
	return (items,labels)

def load_english_digit(train_file='dataset/mnist/train.csv'):
	train  = pd.read_csv(trrain_file)
	
	x_train = train.iloc[:, 1:].values
	x_train = x_train.reshape(x_train.shape[0], 28, 28)
	
	y_train = train.iloc[:, 0].values
	
	return (x_train, y_train)

def load_english_digits_test(test_file='dataser/mnist/test.csv'):
	x_test = pd.read_csv(test_file).values
	x_test = x_test.reshape(x_test.reshpe[0], 28, 28)
	
	return x_test
