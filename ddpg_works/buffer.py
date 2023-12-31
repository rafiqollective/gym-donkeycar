import numpy as np

class ReplayBuffer:
    def __init__(self, max_size, input_shape, n_actions):
        self.mem_size = max_size
        self.mem_cnt = 0
        self.state_memory = np.zeros((self.mem_size,*input_shape), dtype=np.float16)
        self.new_state_memory = np.zeros((self.mem_size, *input_shape),dtype=np.float16)
        self.action_memory = np.zeros((self.mem_size, n_actions),dtype=np.float16)
        self.reward_memory = np.zeros(self.mem_size,dtype=np.float16)
        self.terminal_memory = np.zeros(self.mem_size, dtype = bool)
        
    def store_transition(self, state, action, reward,
                         new_state, done):
        
        index = self.mem_cnt % self.mem_size
        self.state_memory[index] = state
        self.new_state_memory[index] = new_state
        self.action_memory[index] = action
        self.reward_memory[index] = reward
        self.terminal_memory[index] = done

        self.mem_cnt += 1

    def sample_bufer(self, batch_size):

        max_mem = min(self.mem_cnt, self.mem_size)
        batch = np.random.choice(max_mem, batch_size, replace=False)

        states = self.state_memory[batch]
        states_= self.new_state_memory[batch]
        actions = self.action_memory[batch]
        rewards = self.reward_memory[batch]
        dones = self.terminal_memory[batch]

        return states, actions, rewards, states_, dones
        