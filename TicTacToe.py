def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


from time import sleep

def pvp_mode():
    print('Loading...')
    sleep(2.0)
    marker = ''
    global o1, o2
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
        if marker == 'X':
            o1 = 'X'
            o2 = 'O'
        elif marker == 'O':
            o1 = 'O'
            o2 = 'X'


def select_mode():
    print('Welcome to Tic Tac Toe!\nPlese select a game modes\n1) player vs player\n2) computer vs player')
    while True:
        try:
            decision = int(input("Please enter your choice as integer: "))
        except:
            print("Looks like you didn't not enter an integer!")
            continue
        else:
            if decision == 1:
                return decision
            elif decision == 2:
                return decision
            else:
                print('please enter 1 or 2 as your input')
                continue

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def win_check(board, mark):
    return (
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


def full_board_check(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True


def your_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        position = int(input('Choose your next position: (1-9) '))

    return position


# reply = select_mode()
# if reply == 1:
print('Welcome to Tic Tac Toe Game')
while True:
    theBoard = [' '] * 10
    pvp_mode()
    global o1, o2
    turn = choose_first()
    game_on = True

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = your_choice(theBoard)
            theBoard[position] = ol
            if win_check(theBoard, o1):
                display_board(theBoard)
                print(f'{o2} win the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player2's turn.
            display_board(theBoard)
            position = your_choice(theBoard)
            theBoard[position] = o2
            if win_check(theBoard, o2):

                display_board(theBoard)
                print(f'{o2} win has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        print(" -------- End the game --------")
