# Project 3 - Tic-Tac-Toe Simulator - Main Program
#
# Name: Joanna Chou
# Instructor: S. Einakian 
# Section: 07
# Date: 2/9/2022

from tictactoeFuncs import *

def main():
    welcome()
    board_list = create_board()
    print(check_win(board_list))

if __name__ == '__main__':
    main()
