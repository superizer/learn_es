import gym
import numpy as np

env = gym.make('CartPole-v0')

max_reward = 0
max_parameters = []

noise_scaling = 0.1
parameters = np.random.rand(4) * 2 - 1

for i_episode in range(2000):
    observation = env.reset()
    r = 0
    newparams = parameters + (np.random.rand(4) * 2 - 1)*noise_scaling
    for t in range(100):
        env.render()
        print(observation)
        #action = env.action_space.sample()
        action = 0 if np.matmul(parameters,observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        r += reward
        #if done:
        #    print("Episode finished after {} timesteps".format(t+1))
        #    break
    print('reward = ', r)
    if r > max_reward:
        max_reward = r
        max_parameters = parameters
        parameters = newparams

print('max reward = ', max_reward, ' max parameter = ', max_parameters)

