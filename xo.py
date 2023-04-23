
test_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] #setting the gameboard
def gameboard(board):
    print(board[7]+" | "+board[8]+" | "+board[9])
    print("- | - | -")
    print(board[4]+" | "+board[5]+" | "+board[6])
    print("- | - | -")
    print(board[1]+" | "+board[2]+" | "+board[3])
gameboard(test_board)
def check_winner(test_board): #checking for winning combination
        for i in range(len(test_board) - 2):
            if test_board[i] == test_board[i+1] == test_board[i+2] == 'X':
                print(" - - - PLAYER 1 WIN - - - ")
                return True
            elif test_board[i] == test_board[i+1] == test_board[i+2] == 'O':
                print(" - - - PLAYER 2 WIN - - - ")
                return True

game = True
while game: #game process 
    player1_turn = int(input("1 player turn: "))
    while test_board[player1_turn] == 'O':
        print("Choose other number")
        player1_turn = int(input("1 player turn: "))
    test_board[player1_turn] = 'X'
    gameboard(test_board)
    if check_winner(test_board):
        game = False
        break
    player2_turn = int(input("2 player turn: "))
    while test_board[player2_turn] == 'X':
        print("Choose other number")
        player2_turn = int(input("2 player turn: "))
    test_board[player2_turn] = 'O'
    gameboard(test_board)
    if check_winner(test_board):
        game = False
        break
