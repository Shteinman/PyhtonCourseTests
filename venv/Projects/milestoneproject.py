###### TIC TAC TOE GAME #########

#imports
from random import shuffle

#Test Board
test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#Variables
#choice = ''
#loc_choice = ''
#t = []

#Display board
def display_board(board):
    row1 = [board[6],board[7],board[8]]
    row2 = [board[3],board[4],board[5]]
    row3 = [board[0],board[1],board[2]]
    print (' ------------')
    print ('|',board[6],'|',board[7],'|',board[8],'|')
    print (' ------------')
    print ('|',board[3],'|',board[4],'|',board[5],'|')
    print (' ------------')
    print ('|',board[0],'|',board[1],'|',board[2],'|')
    print (' ------------')
#display_board(test_board)

#### Define user choice X or O


def user_choice():

    choice = ''
    # check if choice is within the list
    while choice.upper() not in ['X', 'O']:
        choice = input("Player 1, choose: [X/O] ")

        if choice.upper() not in ['X', 'O']:
            print('Invalid choice!')
    if choice == 'X':
        return ('X','O')
    else:
        return ('O','X')


#user_choice(choice,loc_choice,t)

def place_marker(board, marker, position):
    board[position-1] = marker

#place_marker(test_board, t[0], int(t[1]))


def win_check(board, mark):
    a = 0
    for place in range(0,len(board)-1):
        if place < 3:
            if board[place] == mark:
                if board[place+3] == mark and board[place+6] == mark:
                    print("You've won!")
                    break
        if board[place] == mark:
            a += 1
            if a == 3 and (place == 2 or place == 5 or place == 8):
                print("You've won!")
                break
        if board[4] == mark:
            if (board[0] == mark and board[8] == mark) or (board[2] == mark and board[6] == mark):
                print("You've won!")
                break
        else:
            a = 0



#win_check(test_board,'X')

def who_first(names):
    shuffle(names)
    return names

#print(who_first(['daniel','sasha']))


def space_check(board, position):
    return board[position-1] == ' '

#space_check(test_board, 0)


def full_board_check(board):
    for i in range(0, len(board)):
        if board[i] == ' ':
            return False
    return True


def player_choice(board):
    position = 0
    while position not in range (1,10) or not space_check(board,position):
        position = int(input("Please enter a number (1-9): "))
    return position


def keep_playing():
    choice = ''

    # check if choice is within the list
    while choice.upper() not in ['Y', 'N']:
        choice = input("Would you like to continue? [Y/N] ")

        if choice.upper() not in ['Y', 'N']:
            print('Invalid choice!')
    if choice.upper() == 'Y':
        return True

    else:
        return False


def game():
    print('Welcome to the Jungle!')
    while True:
        ## Set the game (Set board, Who's First, Choose Markers x,o)
        the_board = test_board
        player1_marker,player2_marker = user_choice()

        turn = who_first(['Player 1', 'Player 2'])[0]
        print (turn)
        play_game = input('Are you ready to play? Enter Yes or No.')

        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                display_board(the_board)
                #choose position
                position = player_choice(the_board)
                #Place marker at the position
                place_marker(the_board,player1_marker,position)
                #check win?
                if win_check(the_board,player1_marker):
                    display_board(the_board)
                    print('Player 1, you are the winner!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("It's a tie!")
                        game_on = False
                    else:
                        turn = 'Player 2'


            else:
                display_board(the_board)
                # choose position
                position = player_choice(the_board)
                # Place marker at the position
                place_marker(the_board, player2_marker, position)
                # check win?
                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('Player 2, you are the winner!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("It's a tie!")
                        game_on = False
                    else:
                        turn = 'Player 1'

        if not keep_playing():
            break


game()
