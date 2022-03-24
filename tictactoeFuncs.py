# Project 3 - Tic-Tac-Toe Simulator - Functions
# 
# Name: Joanna Chou
# Instructor: S. Einakian 
# Section: 07
# Date: 2/9/2022

# 1) welcome function - This function welcomes the player and presents rules.
# Signature: None -> int
def welcome():
    print("Welcome to this Tic-Tac-Toe Simulator.")
    print("Your goal is to line up 3 of your tics in either a line or diagonal.")
    print("You will pick either X or O. X will go first.")
    opponent = input("Do you wish to play against a (1) computer, or with (2) Players? ")
    while opponent != "1" and opponent != "2":
        print("Invalid input. Please try again.")
        opponent = input("Do you wish to play against a (1) computer, or with (2) Players? ")
    return opponent

# 2) create_board function - This function creates the Tic-Tac-Toe Board.
# Signature: None -> list
def create_board() -> list:
    print("The board positions are as follows:")
    board = [" "," "," "," "," "," "," "," "," "]
    print("  1  |  2  |  3  ")
    print("-----------------")
    print("  4  |  5  |  6  ")
    print("-----------------")
    print("  7  |  8  |  9  ")
    return board

# 3) print_board function - This function will print the board according to the values the user passes into a list.
def print_board(board: list) -> list:
    index = 0
    for row in (range(0,len(board)//3)):
        print("  "+ board[index] + "  |  " + board[index+1] + "  |  "+ board[index+2]+ "  ")
        if row == (len(board)/3)-1:
            break
        print("-----------------")
        index += 3
    return board

# 4) pick_etter function - This function will ask the user to pick 'X' or 'O.'
# Signature: None -> str
def pick_letter() -> str:
    letter = input("Choose X or O: ")
    while letter != "X" and letter != "O":
        print("Invalid input. Please try again.")
        letter = input("Choose X or O: ")
    return letter

# 5) get_input function - This function takes a letter and the board and asks the user to choose a location on the board.
def get_input(letter: str, board: list) -> list:
    prompt_string = "Where do you like to place your letter (pick in range of 1-9): "
    location = int(input(prompt_string))
    while ((location) < 1) or ((location) > 9) or board[((location))-1] != " ":
        print("Invalid move! Location is already taken. Please try again.")
        location = int(input(prompt_string))
    board[(int(location))-1] = letter
    return board
   
# 6) check_rows function - This function takes the board and returns True and the letter if a row is filled with the same letter.
def check_rows(board: list) -> tuple:
    if board[0] == board[1] == board[2] != " ":
        boolean = True
        letter = board[0]
    elif board[3] == board[4] == board[5] != " ":
        boolean = True
        letter = board[3]
    elif board[6] == board[7] == board[8] != " ":
        boolean = True
        letter = board[6]
    else:
        boolean = False
        letter = None
    return(boolean, letter)

# 7) check_cols function - This function takes the board and returns True and the letter if a column is filled with the same letter.
def check_cols(board: list) -> tuple:
    if board[0] == board[3] == board[6] != " ":
        boolean = True
        letter = board[0]
    elif board[1] == board[4] == board[7] != " ":
        boolean = True
        letter = board[1]
    elif board[2] == board[5] == board[8] != " ":
        boolean = True
        letter = board[2]
    else:
        boolean = False
        letter = None
    return(boolean, letter)
   
# 8) check_diags function - This function takes the board and returns True and the letter if a diagonal is filled with the same letter.
def check_diags(board: list) -> tuple:
    if board[0] == board[4] == board[8] != " ":
        boolean = True
        letter = board[0]
    elif board[2] == board[4] == board[6] != " ":
        boolean = True
        letter = board[2]
    else:
        boolean = False
        letter = None
    return(boolean, letter)
  
# 9) board_full function - This function takes the board and returns True if the board is full.
def board_full(board: list) -> bool:
    for item in board: 
        if item == " ":
            return False
    return True

# 10) check_win function - This function takes the board, keeps track of the player, and returns the result of the game.
def check_win(board: list) -> str:
    letter1 = pick_letter()
    count = 1
    if letter1 == "O":
        letter2 = "X"
        while check_board(board, count) == "Continue":
            if count % 2 == 1:
                print("It's Player 1's (X's) turn!")
                print_board(board)
                location1 = get_input(letter2, board)
                print_board(location1)
                count += 1
            elif count % 2 == 0:
                print("It's Player 2's (O's) turn!")
                print_board(board)
                location2 = get_input(letter1, board)
                print_board(location2)
                count += 1
        return check_board(board, count)
    elif letter1 == "X":
        letter2 = "O"
        while check_board(board, count) == "Continue":
            if count % 2 == 1:
                print("It's Player 1's (X's) turn!")
                print_board(board)
                location1 = get_input(letter1, board)
                print_board(location1)
                count += 1
            elif count % 2 == 0:
                print("It's Player 2's (O's) turn!")
                print_board(board)
                location2 = get_input(letter2, board)
                print_board(location2)
                count += 1
        return check_board(board, count)


# 11) check_board - This function takes in the current board status and the current player, and checks if there is a win (rows, columns, diagonals) and announces the winner, if any.
def check_board(board: list, count: int) -> str:
    if check_rows(board)[0] == True:
        if (count%2 == 0):
            message = "Winner is Player 1 (X)!"
        elif (count % 2 == 1):
            message = "Winner is Player 2 (O)!"
    elif check_cols(board)[0] == True:
        if (count % 2 == 0):
            message = "Winner is Player 1 (X)!"
        elif (count % 2 == 1):
            message = "Winner is Player 2 (O)!"
    elif check_diags(board)[0] == True:
        if (count % 2 == 0):
            message = "Winner is Player 1 (X)!"
        elif (count % 2 == 1):
            message = "Winner is Player 2 (O)!"
    elif board_full(board) == True:
        message = "Draw!"
    else:
        message = "Continue"
    return message
