# Project 3 - Tic-Tac-Toe Simulator - Tests
# 
# Name: Joanna Chou
# Instructor: S. Einakian 
# Section: 07
# Date: 2/9/2022

import unittest
from tictactoeFuncs import *

class TestCases(unittest.TestCase):
   def test_print_board(self):
      self.assertEqual(print_board([" "," "," "," "," "," "," "," "," "]),[" "," "," "," "," "," "," "," "," "])
      self.assertEqual(print_board(["X"," "," ","O"," "," "," "," ","X"]),["X"," "," ","O"," "," "," "," ","X"])
      self.assertEqual(print_board(["X","O","X","O","X","O","X","O","X"]),["X","O","X","O","X","O","X","O","X"]) 
   
   def test_check_rows(self):
      self.assertEqual(check_rows(["X","O","X","O","X","O","X","O","X"]), (False, None))
      self.assertEqual(check_rows(["X","X","X","O","X"," "," ","O"," "]), (True, "X"))
      self.assertEqual(check_rows(["X"," ","X","O","O","O"," ","O","X"]), (True, "O"))

   def test_check_cols(self):
      self.assertEqual(check_cols(["X","O","X","O","X","O","X","O","X"]), (False, None))
      self.assertEqual(check_cols(["O","O","X"," "," ","X"," ","O","X"]), (True, "X"))
      self.assertEqual(check_cols(["X","O","X","O","O","O"," ","O","X"]), (True, "O"))

   def test_check_diags(self):
      self.assertEqual(check_diags(["X","O","X","O","O","O"," ","O","X"]), (False, None))
      self.assertEqual(check_diags(["X","O","X","O","X","O","X","O","X"]), (True, "X"))
      self.assertEqual(check_diags(["O","X","O","X","O","X","O","X","O"]), (True, "O"))

   def test_check_win(self):
      self.assertEqual(check_win(["X","O","X","O","O","O"," ","O","X"], 8), "Winner is Player 1 (X)!")
      self.assertEqual(check_win(["X","O","O","O","X","X","X","O","O"], 3), "Draw!")
      self.assertEqual(check_win([" "," "," "," "," "," "," "," "," "], 1), "Continue")

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

