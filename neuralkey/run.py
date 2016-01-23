__author_ = "Fariz Rahman"

from machine import Machine
import numpy as np
import time

#Machine parameters
k = 100
n = 10
l = 10

#Update rule
update_rules = ['hebbian', 'anti_hebbian', 'random_walk']
update_rule = update_rules[0]

#Create 2 machines
print("Creating machines : k=" + str(k) + ", n=" + str(n) + ", l=" + str(n))
print("Using " + update_rule + " update rule.")
machine1 = Machine(k, n, l)
machine2 = Machine(k, n, l)

#Random number generator
def random():
	return np.random.randint(-l, l, [k, n])

#Function to evaluate the synchronization score between two machines.
def sync_score(m1, m2):
	return 1.0 - np.average(1.0 * np.abs(m1.W - m2.W)/(2 * l - 1))

#Synchronize weights

sync = False # Flag to check if weights are sync
nb_updates = 0 # Update counter
start_time = time.time() # Start time
sync_history = [] # to store the sync score after every update
while(not sync):

	X = random() # Create random vector of dimensions [k, n]

	tauA = machine1(X) # Get output from machine1
	tauB = machine2(X) # Get output from machine2

	machine1.update(tauB, update_rule) # Update machine1 with machine2's output
	machine2.update(tauA, update_rule) # Update machine2 with machine1's output

	nb_updates += 1

	score = 100 * sync_score(machine1, machine2) # Calculate the synchronization of the 2 machines

	sync_history.append(score)

	print ("Synchronization = " + str(score) + " %")

	if score == 100: # If synchronization score is 100%, set sync flag = True
		sync = True

end_time = time.time()
time_taken = end_time - start_time

print ('Machines have been synchronized.')
print ('Time taken = ' + str(time_taken)+ " seconds.")
print ('Updates = ' + str(nb_updates) + ".")

# Plot graph 
import matplotlib.pyplot as mpl
mpl.plot(sync_history)
mpl.show()
