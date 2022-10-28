from classes import *

def Trial_Error_Search_Algorithm(problem):
    # Complete the implementation of the Trial Error algorithm

    state = Node(problem.initial)
    while True:
        if problem.goal_test(state.state):
            return state
        # Write your code below this line!

        # Write your code above this line!

class Digits(Problem):

    def __init__(self):
        # Complete the implementation of initial function by calling
        # the parent constructor and initialize the initial state and set of goal states

        self.wrong_numbers = [(6,6,6),(6,6,7)]
        self.s4 = 0
        # Write your code below this line!
        pass
        # Write your code above this line! Delete the 'pass' keyword!

    def actions(self, state):
        # Complete the remaining part of the action function
        s1, s2, s3 = state
        acts = []

        if (s1 + 1, s2, s3) not in self.wrong_numbers and self.s4 != 1 and s1 + 1 <= 9:
            acts.append('s1_plus')
        # Write your code below this line!

        # Write your code above this line!
        return acts

    def result(self, state, action):
        # Complete the implementation of result function
        s1, s2, s3 = state
        if action == 's1_plus':
            self.s4 = 1
            return (s1 + 1, s2, s3)
        # Write your code below this line!

        # Write your code above this line!

def main():
    # DO NOT EDIT this function!

    # 1. Exercise: Fill the missing parts of init method (2 points)
    d = Digits()
    print(d.initial, d.goal) # Expected output: (5, 6, 7) [(7, 7, 7)]
    # 2. Exercise: Fill the missing parts of actions method (3 points)
    print(d.actions(d.initial)) # Expected output: ['s1_minus', 's2_plus', 's2_minus', 's3_plus', 's3_minus']
    # 3. Exercise: Fill te missing parts of result method (3 points)
    print(d.result(d.initial, 's2,minus')) # Expected output: (5, 5, 7)
    # 4. Exercise: Fill the missing parts of Trial Error function (2 points)
    print(Trial_Error_Search_Algorithm(d)) # Expected output: <Node (7, 7, 7)>

if __name__ == '__main__':
    main()