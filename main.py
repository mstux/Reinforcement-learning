import numpy as np
import keras
import matplotlib.pyplot as plt

from environment import Environment
from agent import Agent

episodes = 2000

env = Environment()
otto = Agent()

for e in range(episodes):

	state = env.reset()
	state = np.reshape(state, [1, 4])

	for time in range(100):
		action = otto.act(state)
		next_state, reward, done = env.step(action)
		next_state = np.reshape(next_state, [1, 4])
		otto.remember(state, action, reward, next_state, done)
		state = next_state
		
		#if e==episodes-1:
			#plt.figure(1)
			#plt.plot(state[0,0],state[0,1],'ro',state[0,2],state[0,3],'bh')

		if done:
			print(e,time,state[0,2:])
			break
			
	if e>10:
		otto.replay(32)
			
#plt.show()
