import numpy as np 

from matplotlib import pyplot as plt 

step = 150
number_of_samples = step*np.array([1,2,3,4,5,6,7,8,9,10])
train_costs = np.loadtxt("gmm_train_costs")
test_costs  = np.loadtxt("gmm_test_costs")
plt.plot(number_of_samples, train_costs, label='training curve')
plt.plot(number_of_samples, test_costs, label='testing curve')
plt.legend(loc='center right')
plt.show()

