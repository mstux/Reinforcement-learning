import numpy as np
import random

class Environment:
	def reset(self):
		self.done = False
		self.hand_xpos = 0
		self.hand_ypos = 0
		self.goal_xpos = random.randint(-10, 10)
		self.goal_ypos = random.randint(-10, 10)
		self.state = np.array([self.hand_xpos, self.hand_ypos, self.goal_xpos, self.goal_ypos])
		return self.state
		
	def step(self,action):
		# 4 actions, up down left right
		if (action == 0):
			self.new_hand_xpos = self.hand_xpos
			self.new_hand_ypos = self.hand_ypos+1
		elif (action == 1):
			self.new_hand_xpos = self.hand_xpos
			self.new_hand_ypos = self.hand_ypos-1
		elif (action == 2):
			self.new_hand_ypos = self.hand_ypos
			self.new_hand_xpos = self.hand_xpos-1
		elif (action == 3):
			self.new_hand_ypos = self.hand_ypos
			self.new_hand_xpos = self.hand_xpos+1
		
		self.hand_pos = np.array([self.hand_xpos, self.hand_ypos])
		self.new_hand_pos = np.array([self.new_hand_xpos, self.new_hand_ypos])
		self.goal_pos = np.array([self.goal_xpos, self.goal_ypos])
		self.d = np.linalg.norm(self.hand_pos - self.goal_pos)
		self.new_d = np.linalg.norm(self.new_hand_pos - self.goal_pos)
		
		if (self.new_d == 0):
			self.reward = 10
			self.done = True
		elif (self.new_d < self.d):
			self.reward = 1
		elif (self.new_d >= self.d):
			self.reward = -1

		self.next_state=np.append(self.new_hand_pos, self.goal_pos)
		
		if (action == 0):
			self.hand_ypos = self.hand_ypos+1
		elif (action == 1):
			self.hand_ypos = self.hand_ypos-1
		elif (action == 2):
			self.hand_xpos = self.hand_xpos-1
		elif (action == 3):
			self.hand_xpos = self.hand_xpos+1

		return self.next_state, self.reward, self.done
		
#env = Environment()
#env.reset()
#print(env.state)
#print(env.step(0))