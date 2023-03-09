#
# state.py (Final project)
#
# A State class for the Eight Puzzle
#
# name: Aarsh Mehta
# email: aarsh@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Nupur Divekar
# partner's email: ndivkar@bu.edu
#

from board import *

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###
    def __init__(self, board, predecessor, move):
        'constructs a new State object by initializing the above four fields/attributes'
        self.board = board
        self.predecessor = predecessor
        self.move = move
        if predecessor == None:
            self.num_moves = 0
        else:
            self.num_moves = predecessor.num_moves+1
        

    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True
    
    def is_goal(self):
        'returns True if the called State object is a goal state, and False otherwise'
        return GOAL_TILES == self.board.tiles
    
    def generate_successors(self):
        'creates and returns a list of State objects for all successor states of the called State object'
        successors = []
        for i in MOVES:
            b = self.board.copy()
            if b.move_blank(i) == True:
                s = State(b, self, i)
                successors += [s]
        return successors
    
    def print_moves_to(self):
        'prints the sequence of moves that lead from the initial state to the called State object'
        if self.predecessor == None:
            print('initial state:')
            print(self.board)
        else:
            self.predecessor.print_moves_to()
            if self.move == 'up':
                print('move the blank up:')
            if self.move == 'down':
                print('move the blank down:')
            if self.move == 'right':
                print('move the blank right:')
            if self.move == 'left':
                print('move the blank left:')
            print(self.board)
                