

# initializing required
print('Tic Tac Toe Game Starts')
current_state = ['_','_','_','_','_','_','_','_','_']
playerone = []
playertwo = []


# getting names of the players

a = input('Player one, enter your name')

if(a == ''):
    a = 'Player One'

b = input('Player two, enter your name')

if(b == ''):
    b = 'Player Two'


print('Remember corresponding number to position')
print(''' 
    
    1_ 2_ 3_
    4_ 5_ 6_
    7_ 8_ 9_
    
    ''')


# Checks whether the entered move is possible or invalid
isMovePossible = lambda k : not (k in playerone or k in playertwo) and (0<k<10) 
    
    
# Prints the current state of the game
def printCurrentState():
    print('''
          
     %s %s %s
     %s %s %s
     %s %s %s
    
    '''%(current_state[0], current_state[1], current_state[2],current_state[3], current_state[4], current_state[5],
    current_state[6], current_state[7], current_state[8]))


# checks if their is a winner after every move
def checkWinner(playerNumber):
    k = 0
    if(playerNumber == 1):
        player = playerone
    else:
        player = playertwo
        
    
    for a in [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
        if(a[0] in player and a[1] in player and a[2] in player):
            k = 1
    return True if k == 1 else False
            




# i is move number   
i = 1


# game starts here
while True:
    if(i%2 == 1):    
        k = input("%s: Choose you option"%(a))
        if(k==''):
            print('Invalid Move')
            continue
        if(isMovePossible(int(k))):
            current_state[int(k)-1] = 'O'
            playerone.append(int(k))
        else:
            print('Invalid Move')
            continue
    else:
        if(k==''):
            print('Invalid Move')
            continue
        k = input("%s: Choose you option"%(b))
        if(isMovePossible(int(k))):
            current_state[int(k)-1] = 'X'
            playertwo.append(int(k))
        else:
            print('Invalid Move')
            continue
    printCurrentState()
    if(checkWinner(i%2)):
        print('%s WON THE GAME'%(a.upper() if i%2 == 1 else b.upper()))
        break
    
    if(i == 9):
        print('GAME OVER')
    
    i += 1
    
    
    
    
    

    
    
        