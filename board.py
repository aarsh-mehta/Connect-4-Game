# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(3):
            for c in range(3):
                self.tiles[r][c]= str(int(digitstr[3*r+c]))
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c
    
    def __repr__(self):
        'returns a string representation of a Board object'
        string = ""
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    string += "_ "
                else:
                    string += str(self.tiles[r][c]) + " "
            string += "\n"
        return string
    
    def move_blank(self, direction):
        'takes as input a string direction that specifies the direction in which the blank should move, and that attempts to modify the contents of the called Board object accordingly.'
        if(direction=='up'):
            if self.blank_r == 0:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c]=self.tiles[self.blank_r - 1][self.blank_c]
                self.tiles[self.blank_r - 1][self.blank_c] = '0'
                self.blank_r=self.blank_r - 1
                self.blank_c=self.blank_c
                return True
        
        elif(direction=='down'):
            if self.blank_r == 2:
                return False
            else: 
                self.tiles[self.blank_r][self.blank_c]=self.tiles[self.blank_r + 1][self.blank_c]
                self.tiles[self.blank_r + 1][self.blank_c] = '0'
                self.blank_r=self.blank_r + 1
                self.blank_c=self.blank_c
                return True
            
        elif(direction=='left'):
            if self.blank_c == 0:
               return False
            else:
                self.tiles[self.blank_r][self.blank_c]=self.tiles[self.blank_r][self.blank_c - 1]
                self.tiles[self.blank_r][self.blank_c - 1] = '0'
                self.blank_r=self.blank_r
                self.blank_c=self.blank_c - 1
                return True
            
        elif(direction=='right'):
            if self.blank_c == 2:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c]=self.tiles[self.blank_r][self.blank_c + 1]
                self.tiles[self.blank_r][self.blank_c + 1] = '0'
                self.blank_r=self.blank_r
                self.blank_c=self.blank_c + 1
                return True
            
        else: 
            return False
        
    def digit_string(self):
        ' creates and returns a string of digits that corresponds to the current contents of the called Board object’s tiles attribute'
        string= ''
        for r in range(3):
            for c in range(3):
                string+=str(self.tiles[r][c])
        return string
    
    def copy(self):
        'returns a newly-constructed Board object that is a deep copy of the called object'
        copy = Board(self.digit_string())
        return copy
    
    def num_misplaced(self):
        'counts and returns the number of tiles in the called Board object that are not where they should be in the goal state'
        count = 0
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    count = count
                elif self.tiles[r][c] != GOAL_TILES[r][c]:
                    count +=1
        return count
    
    def __eq__(self, other):
        'can be called when the == operator is used to compare two Board objects'
        if self.tiles == other.tiles:
            return True
        else:
            return False
        
    def position_point_allocator(self):
        'allocates points based on the position of the tile; +2 pointsif its out of its row and column and +1 points if its either out of its row or column'
        points=0
        
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0' or self.tiles[r][c] == GOAL_TILES[r][c]:
                    points = points
                else:
                    if self.tiles[r][c] == '1':
                        if r != 0 and c != 1:
                            points +=2
                        elif r != 0:
                            points +=1
                        elif c != 1:
                            points +=1
                    elif self.tiles[r][c] == '2':
                        if r != 0 and c != 2:
                            points +=2
                        elif r != 0:
                            points +=1
                        elif c != 2:
                            points +=1
                    elif self.tiles[r][c] == '3':
                        if r != 1 and c != 0:
                            points +=2
                        elif r != 1:
                            points +=1
                        elif c != 0:
                            points +=1
                    elif self.tiles[r][c] == '4':
                        if r != 1 and c != 1:
                            points +=2
                        elif r != 1:
                            points +=1
                        elif c != 1:
                            points +=1
                    elif self.tiles[r][c] == '5':
                        if r != 1 and c != 2:
                            points +=2
                        elif r != 1:
                            points +=1
                        elif c != 2:
                            points +=1
                    elif self.tiles[r][c] == '6':
                        if r != 2 and c != 0:
                            points +=2
                        elif r != 2:
                            points +=1
                        elif c != 0:
                            points +=1
                    elif self.tiles[r][c] == '7':
                        if r != 2 and c != 1:
                            points +=2
                        elif r != 2:
                            points +=1
                        elif c != 1:
                            points +=1
                    elif self.tiles[r][c] == '8':
                        if r != 2 and c != 2:
                            points +=2
                        elif r != 2:
                            points +=1
                        elif c != 2:
                            points +=1
        return points
        
        
    