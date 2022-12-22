# Michael Higley 
# Started 12/20/2022 -Generated simple game board with 2 players and terrain
# 12/22/2022 - Added more organizational functions and comments
# 11x11 grid, one seeker one hider. 3 randomly generated terrain appear every turn on the hiders turn.
#  if the hider "hides" behind the terrain, the seeker cannot see the hider. Both players can move like a queen in chess and if the hider is caught the games ends.
# Seeker wins by avoiding for a certain amount of turns
# 0 in array means empty, ! in array for seeker, 2 for hider, 3 for terrain 

import numpy as np
defaultnumTerrain = 3

#Creates random x and y coordinates for terrain
#Variable amount of terrain created
def createTerrain(numTerrain):
    for i in range(numTerrain):
        a = np.random.randint(1,10)
        b = np.random.randint(1,10)
    #Testing terrain num
        #print(a,b)
        if (board[a][b] == 0):
            board[a][b] = 3
            #numTerrain -= 1
        else :
            numTerrain += 1 

#Hiders turn takes input as x and y coordinate
def hiderTurn(start):
    move1 = input("Enter coordinate x")
    move2 = input("Enter coordinate y")
    end = (move1,move2)
    #Check if end location is viable based on start location
    #Needs to move like a queen in chess (Horizontal, Vertical, Diagonal, and unable to pass through terrain)

#Returns hider location as x and y
def getHider():
    return hiderLocation
#Sets hider location after changes
def setHider(x,y):
    hiderLocation = (x,y)

#Creates game board array
rows, cols = (11, 11)
board = [[0 for i in range(cols)] for j in range(rows)]

#Generates seeker in middle of board
board[5][5] = 1

#Generates hider in random place on board
x = np.random.randint(1,10)
y = np.random.randint(1,10)
board[x][y] = 2
hiderLocation = (x,y)
#print(hiderLocation)

#Generates 3 random terrain
createTerrain(defaultnumTerrain)

#Prints board
for i in range(len(board)): 
    for j in range(len(board[i])): 
        print(board[i][j], end="  ")
    print() 


