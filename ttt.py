import random
from IPython.display import clear_output

def display_board():
    clear_output()
    print(f' {f[1]} | {f[2]} | {f[3]} \n-----------\n {f[4]} | {f[5]} | {f[6]} \n-----------\n {f[7]} | {f[8]} | {f[9]} \n')
    
def player_input():
    players = ["X","O"]
    
    while len(players) == 2:
        global p1
        imp = input('Enter a marker for player 1: ').upper()
        if imp in players:
            p1 = imp
            players.remove(imp)
            player_1 = p1
        else:
            p1 = input('please enter X or O: ').upper()
            player_1 = p1
    global p2
    p2 = players[0]
    print(f'Player 2, you are {p2}')
    return p1, p2
        

    
def place_marker(marker, position):
    del f[int(position)]
    f.insert(int(position), marker)
    board = f' {f[1]} | {f[2]} | {f[3]} \n-----------\n {f[4]} | {f[5]} | {f[6]} \n-----------\n {f[7]} | {f[8]} | {f[9]} \n'
    
def win_check():
    global on
    on = True
    #
    # check horizontal triplets
    #
    if str(f[1]) == str(f[2]) == str(f[3]) == marker:
        on = False
        print(f'{marker} wins the game')
    
    if str(f[4]) == str(f[5]) == str(f[6]) == marker:
        on = False
        print(f'{marker} wins the game')
    
    if str(f[7]) == str(f[8]) == str(f[9]) == marker:
        on = False
        print(f'{marker} wins the game')
    #
    # check vertical triplets    
    #
    if str(f[1]) == str(f[4]) == str(f[7]) == marker:
        on = False
        print(f'{marker} wins the game')
    
    if str(f[2]) == str(f[5]) == str(f[8]) == marker:
        on = False
        print(f'{marker} wins the game')

    if str(f[3]) == str(f[6]) == str(f[9]) == marker:
        on = False
        print(f'{marker} wins the game')
    #    
    # check diagonals
    #
    if str(f[1]) == str(f[5]) == str(f[9]) == marker:
        on = False
        print(f'{marker} wins the game')
    
    if str(f[7]) == str(f[5]) == str(f[3]) == marker:
        on = False
        print(f'{marker} wins the game!')
    return on
    
def choose_first():
    if random.randint(0, 1) == 0:
        return 'p1'
    else:
        return 'p2'
    
def space_check(position):
    global clear
    clear = False
    if f[int(position)] == ' ':
        clear = True
    else:
        print('That space is taken, choose another')
        player_choice(p1)
    return clear

def full_board_check():
    full_board = False
    if ' ' in f[1:]:
        full_board = False
    else:
        full_board = True
    return full_board

def player_choice(p):
    global position
    position = 0
    position = input('Choose a position to fill (1-9): ')
    space_check(int(position))
    place_marker(p, int(position))
    
    
    #while position not in [1,2,3,4,5,6,7,8,9] or not space_check(position):
     #   position = input('Choose a position to fill (1-9): ')
    
    #place_marker(p, int(position))
    
def replay():
    replay_bool = False

    replay = input("Would you like to play again? (Y or N): ")
    
    if replay.upper() == 'Y':
        replay_bool = True
    else:
        replay_bool = False
        print('Thanks!')
    return replay_bool



## GAME

print('Welcome to Tic Tac Toe!')

global f
f = [' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ']
player_t = [1,2,1,2,1,2,1,2,1]

on = True

player_input()

while on:
    display_board()
    print('Player 1:')
    marker = p1
    player_choice(marker)
    if clear:
        place_marker(marker, position)
    controller = p2
    if not win_check():
        break
        #if full_board_check():
          #  break
    
    full_board_check()
    display_board()
    print('Player 2:')
    marker = p2
    player_choice(marker)
    if clear:
        place_marker(marker, position)
    if not win_check():
        break
        #if full_board_check():
    
display_board()
win_check()

replay()
if replay():
    on = True
else: 
    on = False