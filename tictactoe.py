"""
Tic Tac Toe Player
"""

import copy
from random import choice

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    X is X, O is O
    """
    xs = 0
    os = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X:
                xs += 1
            elif board[i][j] == O:
                os += 1
    if (xs + os) % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    i is the row, j is the cell in the row.
    """
    spaces = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                space = (i, j)
                spaces.add(space)
    return spaces


def result(original_board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Make a deep copy of the board per instructions
    possible_board = copy.deepcopy(original_board)

    i = action[0]
    j = action[1]

    # Check if space is already taken
    if possible_board[i][j] != EMPTY:
        raise ValueError("space taken")
    
    # Determine whose turn it is and play the turn
    if player(possible_board) == X:
        possible_board[i][j] = X
    else:
        possible_board[i][j] = O
    return possible_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    X if X, O if O, None if no one.
    """
    
    # Vertical Wins
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
    
    # Horizontal Wins
    for j in range(len(board)):
        if board[0][j] == board[1][j] and board[0][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
    
    # Diagonal Wins
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        if board[1][1] == X:
            return X
        elif board[1][1] == O:
            return O

    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    # Check if win
    if winner(board):
        return True

    # Check if there is an empty space
    for row in board:
        if EMPTY in row:
            return False

    # If the board is full
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    alpha = float('-inf')
    beta = float('inf')
    best_move = (1, 1)
    
    if player(board) == X:
        v = float('-inf')
        for action in actions(board):
            if v < min_value(result(board, action), alpha, beta):
                v = min_value(result(board, action), alpha, beta)
                best_move = action
        return best_move
    if player(board) == O:
        v = float('inf')
        for action in actions(board):
            if v > max_value(result(board, action), alpha, beta):
                v = max_value(result(board, action), alpha, beta)
                best_move = action
        return best_move


def max_value(board, alpha, beta):
    '''
    Finds the max value of all possible moves on the board
    '''
    if terminal(board):
        return utility(board)
    
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        if v >= beta:
            break
        alpha = max(alpha, v)
    return v


def min_value(board, alpha, beta):
    '''
    Finds the min value of all possible moves on the board
    '''
    if terminal(board):
        return utility(board)
    
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        if v <= alpha:
            break
        beta = min(beta, v)
    return v