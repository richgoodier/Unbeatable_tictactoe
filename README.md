# Unbeatable Tic-Tac-Toe
This project is an implementation of a Tic-Tac-Toe game with an AI opponent. The AI uses the Minimax algorithm to determine its moves, making it play optimally.

## Overview of Functions in tictactoe.py
The functions in `tictactoe.py` are defined as follows:

- `player(board)`: Returns which player's turn it is.
- `actions(board)`: Returns a set of all possible actions (i, j) on the board.
- `result(board, action)`: Returns the resulting board state after the action has been performed.
- `winner(board)`: Returns the winner of the game if there is one.
- `terminal(board)`: Returns a boolean indicating whether the game is over.
- `utility(board)`: Returns the utility of the board.
- `minimax(board)`: Returns the optimal action for the player to move on the board.

These functions form the backbone of the Tic-Tac-Toe game and the Minimax AI.

Please note that the game is unbeatable given optimal play from both sides. This means if you play optimally as well, the best outcome you can achieve is a tie.

## Required Libraries

This project requires Python 3.10 and Pygame to be installed.

## Disclaimer
Please note that the problem set specifications are owned by [Harvard University](https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/) and this solution is only meant as a guide, not for plagiarism.
