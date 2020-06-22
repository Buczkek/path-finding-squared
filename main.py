import sys


WALL = 1


board = [
         [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
         [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0],
         [0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0],
         [0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],
         [0,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
         [0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
         [0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
         ]

crossable = [0]

if len(board) == 0:
    sys.exit(1)
    
new = []
size = (len(board[0]), len(board))

def spread(cords, finish):
    global size
    global reached
    global values
    x, y = cords
    if reached:
        return None
    if cords == finish:
        reached = True






        
##    v = values[cords]
##    if 0 <= x-1 <= size[0] and (x-1, y) not in values and (
##        board[x-1][y] in crossable):
##        spread((x-1, y))
##    if 0 <= cords[1]-1 <= size[1] and (cords[1]-1, cords[1]) not in values and (
##        board[cords[0]-1][cords[1]]):
##        spread((cords[0]-1, cords[1]))
##    if 0 <= cords[0]-1 <= size[0] and (cords[0]-1, cords[1]) not in values and (
##        board[cords[0]-1][cords[1]]):
##        spread((cords[0]-1, cords[1]))
##    if 0 <= cords[0]-1 <= size[0] and (cords[0]-1, cords[1]) not in values and (
##        board[cords[0]-1][cords[1]]):
##        spread((cords[0]-1, cords[1]))
##        
    

def find_path(board, start, finish):

    global reached
    global new
    
    reached = False
    
    global values
    values = {}

    spread(start)
    
    
    
##    new = [start]

    
        
