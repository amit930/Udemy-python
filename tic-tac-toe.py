import random

def print_board(available, board):
    # Prepare board
    print('\n\nAvailable          Board\n\n')
    print(available[7]+'|',available[8]+'|',available[9], '         ', board[7]+'|', board[8]+'|', board[9])
    print("--------         --------")
    print(available[4]+'|',available[5]+'|',available[6], '         ', board[4]+'|', board[5]+'|', board[6])
    print("--------         --------")
    print(available[1]+'|',available[2]+'|',available[3], '         ', board[1]+'|', board[2]+'|', board[3])
    print('\n\n')

def player_input():
    #Keep taking input until a valid input is choosed by the user
    while True:
        choice = input("Please enter the marker of your choice (X) or (O)")
        if choice == 'X' or choice == 'O' or choice == '#':
            return choice
        else:
            print('Invalid choice. Try again (Press # for exit)')

def isEmpty(board, pos):
    return board[pos] == ' '

def player_choice(board):
    pos = 0
    while pos not in range(1,10) or not isEmpty(board, pos):
        pos = int(input("Enter the position in board:: "))
    return pos

def check_status(board, sign):
    return ((board[1] == sign and board[2] == sign and board[3] == sign) or
           (board[4] == sign and board[5] == sign and board[6] == sign) or
           (board[7] == sign and board[8] == sign and board[9] == sign) or
           (board[1] == sign and board[4] == sign and board[7] == sign) or
           (board[2] == sign and board[5] == sign and board[8] == sign) or
           (board[3] == sign and board[6] == sign and board[9] == sign) or
           (board[7] == sign and board[5] == sign and board[3] == sign) or
           (board[1] == sign and board[5] == sign and board[9] == sign))

def isboardfull(board):
    for i in range(1,10):
        if isEmpty(board, i) == True:
            return False
    else:
        return True

def choose_first():
    if random.randint(0, 1) == 0:
        return 'User_2'
    else:
        return 'User_1'

def replay():
    return input("Want to play again: (y/n)").lower().startswith('y')

def tictactoe():
    while True:
        print('\n\nWelcome to Tic-Tac-toe!\n\n')
        #Prepare the board
        board = [' '] * 10
        available = [str(x) for x in range(0,10)]
        print_board(available, board)
        c = player_input()
        if  c == '#':
            print("Exitig...")
            return
        if c == 'X':
            player_1_option, player_2_option = 'X', 'O'
        else:
            player_1_option, player_2_option = 'O', 'X'

        print("\nStarting Game with user1 as {} and user2 as {}\n".format(player_1_option, player_2_option))
        turn = choose_first()
        print(turn + " will go first\n")
        yes = input("\nAre you ready! (y/n)")
        if yes[0].lower() == 'y':
            gameon = True
        else:
            gameon = False
        while gameon:
            print_board(available, board)
            print(turn + "'s turn\n")

            if turn == 'User_1':
                # User 1 turn
                pos = player_choice(board)
                board[pos] = player_1_option
                available[pos] = ' '
                if check_status(board, player_1_option):
                    print_board(available, board)
                    print('Congratulations! User_1 has won the game')
                    gameon = False
                elif isboardfull(board):
                    print_board(available, board)
                    print('Draw!!')
                    gameon = False
                else:
                    turn = "User_2"

            elif turn == 'User_2':
                # User 2 turn
                pos = player_choice(board)
                board[pos] = player_2_option
                available[pos] = ' '
                if check_status(board, player_2_option):
                    print_board(available, board)
                    print('Congratulations! User_2 has won the game')
                    gameon = False
                elif isboardfull(board):
                    print_board(available, board)
                    print('Draw!!')
                    gameon = False
                else:
                    turn = "User_1"

        if not replay():
            #Want to play again
            break
            
tictactoe()
