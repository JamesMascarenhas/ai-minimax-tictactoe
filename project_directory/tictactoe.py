"""
Tic Tac Toe Player
"""

import math
import copy

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
    """

    xCount = 0
    oCount = 0

    for row in board:
        for cell in row:
            if cell == X:
                xCount += 1
            elif cell == O:
                oCount += 1

    if xCount == oCount:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    pActions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                pActions.add((i, j))
    return pActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise ValueError("Invalid action")
    
    updatedBoard = copy.deepcopy(board)
    updatedBoard[action[0]][action[1]] = player(board)
    
    return updatedBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check Horizontals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
    
    # Check Verticals
    for j in range(3): 
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]
    
    # Check Diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    # No winner yet
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True

    if not actions(board):
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    w = winner(board)
   
    if terminal(board) is True:
        if w == X:
            return 1
        elif w == O:
            return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    if player(board) == X:
        return max_value(board, -math.inf, math.inf)[1]
    else:
        return min_value(board, -math.inf, math.inf)[1]

def max_value(board, alpha, beta):
    """
    Maximizing player (X).
    """
    if terminal(board):
        return [utility(board), None]  # Return as a list
    v = -math.inf
    best_move = None
    for action in actions(board):
        test_value = min_value(result(board, action), alpha, beta)[0]
        if test_value > v:
            v = test_value
            best_move = action
        alpha = max(alpha, v)
        if alpha >= beta:  # Prune the branch
            break
    return [v, best_move]

def min_value(board, alpha, beta):
    """
    Minimizing player (O).
    """
    if terminal(board):
        return [utility(board), None]  # Return as a list
    v = math.inf
    best_move = None
    for action in actions(board):
        test_value = max_value(result(board, action), alpha, beta)[0]
        if test_value < v:
            v = test_value
            best_move = action
        beta = min(beta, v)
        if alpha >= beta:  # Prune the branch
            break
    return [v, best_move]
