from classes import *

def Hill_Climbing_Algorithm(problem):
    # Fill the missing parts of the Hill Climbing search algorithm

    node = Node(problem.initial)
    while True:
        if problem.goal_test(node.state):
            return node
        # Write your code below this line!

        # Write your code above this line!

class TurningCups(Problem):

    def __init__(self):
        # Complete the implementation of initial function by calling
        # the parent constructor and initialize the initial state and set of goal states

        # Write your code below this line!
        pass
        # Write your code above this line! Delete the 'pass' keyword!

    def actions(self, state):
        # Complete the implementation of possible operations
        acts = []
        # Write your code below this line!

        # Write your code above this line!
        return acts

    def result(self, state, action):
        # Fill the missing parts of the transition function
        
        i, j = action
        new_state = list(state)
        # Write your code below this line!

        # Write your code above this line!
        return tuple(new_state)

    def value(self, state):
        num_of_stems = 0
        for i in range(4):
            if state[i] == 0:
                num_of_stems += 1
        return num_of_stems

def main():
    # DO NOT EDIT this function!

    # 1. Exercise: Fill the missing parts of init method (2 points)
    t = TurningCups()
    print(t.initial, t.goal) # Expected output: (0,0,0,0,0,0), [(1,1,1,1,1,1)]
    # 2. Exercise: Fill the missing parts of actions method (3 points)
    print(t.actions(t.initial)) # Expected output: [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3),..., (6, 4), (6, 5)]
    # 3. Exercise: Fill te missing parts of result method (3 points)
    print(t.result(t.initial, (2,3))) # Expected output: (0, 1, 1, 0, 0, 0)
    # 4. Exercise: Fill the missing parts of Hill Climbing function (2 points)
    print(Hill_Climbing_Algorithm(t)) # Expected output: <Node (1, 1, 1, 1, 1, 1)>


if __name__ == '__main__':
    main()