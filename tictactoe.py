"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

num_empty_cells = 9

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def count_empty_cells(board):
    #count empty cell
    global num_empty_cells
    num_empty_cells = 9
    for col_elem in board:
        for col_row in col_elem:
            if col_row != EMPTY:
                num_empty_cells -= 1
    print("the number of empty cells is: ", num_empty_cells)

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #if terminal board true = return none
    #count how many empty space
    # 9 -> x, 8 -> O, 7 -> X ...
    #return X or O
    count_x = 0
    count_o = 0

    for col_elem in board:
        for col_row in col_elem:
            if col_row == X:
                count_x += 1
            if col_row == O:
                count_o += 1

    if terminal(board) == True:
        print("terminal board:", terminal(board))
        return None
    elif count_x <= count_o:
        print ("X player turn, count", count_x)
        #ganjil means x turn
        return X
    else:
        print ("O player turn, count:", count_o)
        #genap means O turn
        return O
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #return a list of with the position of EMPTY cells

    actions_set = set() 
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i, j))
    #print(actions_set)
    return actions_set



def result(board, action):
    """
    The result function takes a board and an action as input, 
    and should return a new board state, without modifying the original board.
        Importantly, the original board should be left unmodified: 
    since Minimax will ultimately require considering many different board states during its computation. 
    This means that simply updating a cell in board itself is not a correct implementation of the result function. 
    You’ll likely want to make a deep copy of the board first before making any changes.
    """
    #create a deep copy of board
    deep_board = copy.deepcopy(board)

    i, j = action
    #check which player makes the move
    current_player = player(board)
    #print(current_player)
    #check if action cell is not empty
    if (deep_board[i][j]) != EMPTY:
        print("cell", i, j, "has been filled")
        #If action is not a valid action for the board, your program should raise an exception.
        #raise ValueError("Illegal Move")
    #change the cell with the symbol of the player
    else: 
        deep_board[i][j] = current_player
    #print(board)
    """
    The returned board state should be the board that would result from taking the original input board, 
    and letting the player whose turn it is make their move at the cell indicated by the input action.
    """
    return deep_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #one can win the game with 3 of their moves vertically, horizontall, or diagonnaly.
    #winning vertically
    #at most, there is only 1 winner. 
    #return X or O -> the winner
    #check if there is any same symbols vertically, horizontally, or diagonally
    symbols = (X, O)

    #winning vertically and horizontally
    for symbol in symbols:
        for i in range(3):
            if (str(board[i][0]) == str(board[i][1]) == str(board[i][2]) == symbol):
                return symbol
            elif (str(board[0][i]) == str(board[1][i]) == str(board[2][i]) == symbol):
                return symbol
    #winning diagonally
            elif (str(board[0][0]) == str(board[1][1]) == str(board[2][2]) == symbol):
                return symbol
            elif (str(board[2][0]) == str(board[1][1]) == str(board[0][2]) == symbol):
                return symbol
            else:
                print("winner(board) = None")
                return None

    #if there is no winner yet, return None
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #if board is full, game over
    if winner(board)!=None or (num_empty_cells <= 0 and winner(board)==None):
        return True
    else: 
        return False

    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    else:
        return 0

    #raise NotImplementedError

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    if (current_player == X):
        max_action = None
        v = -9999
        for action in actions (board):
            if (v < min_value( result( board, action))): 
                # update v
                v = min_value( result( board, action))
                # update action
                max_action = action
        return max_action
    
    else:
        min_action = None
        v = 9999
        for action in actions (board):
            if (v > max_value( result( board, action))): 
                # update v
                v = max_value( result( board, action))
                # update action
                min_action = action
        return min_action
    
    #raise NotImplementedError

def max_value(board):
    """
    Return the max value of a set of result from actions
    """
    v = -9999

    if terminal(board) == True:
        print("terminal board:", terminal(board))
    return utility(board)

    for action in actions(board):
        v = max(v, min_value( result(board, action)))
    return v

def min_value(board):
    """
    Return the lowest value of a set of result from actions
    """
    v = 9999

    if terminal(board) == True:
        print("terminal board:", terminal(board))
    return utility(board)

    for action in actions(board):
        v = min(v, max_value( result(board, action) ))
    return v