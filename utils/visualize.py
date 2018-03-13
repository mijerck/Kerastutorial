import matplotlib.pyplot as plt
import random

# Make figure bigger
plt.rcParams['figure.figsize'] = (20.0, 10.0)

def show_sample(images, labels=None):
	for i in range(0,12):
		random_idx = random.randint(0, len(images))
		
		sp = plt.subplot(3, 4, 1 + i)
		if labels is not  None:
			sp.set_title(labels[random_idx], fontsize=16)
		
		sp.axis('off')
		plt.imshow(images[random_idx])
		
	
def show_sample_incorrect(data, incorrect_indices, actual,
						 predction):
	for i in range(0, 12):
		random_idx = random.choice(incorrect_indices)
		
		sp = plt.subplot(3, 4, 1 + i)
		sp.set_title("Actual: %s\nPredicted: %s" 
					 %(actual[random_idx], 
					   prediction[rando_idx]),fontsize=16)
		sp.axis('off')
		plt.imshow(data[random_idx])
					 

def plot_image(image):
	plt.imshow(image)
					 
def plot_predition(p):
	plt.plot(p[0])
					 
					 
					 