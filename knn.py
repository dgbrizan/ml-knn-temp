import numpy as np

class KNN:

	def __init__(self, k, random_state=None):
		self.k = k
		self.random_state = random_state
		self.labels_ = None
		# YOUR ADDITIONAL CODE HERE


	def fit(self, features: np.ndarray, labels: np.ndarray) -> None:
		'''
		Create the KNN model (or not)
		'''
		# YOUR CODE HERE


	def predict(self, features: np.ndarray) -> np.array:
		'''
		Predict the labels for the input features given the
		training instances.
		'''
		# YOUR CODE HERE

