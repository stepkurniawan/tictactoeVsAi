"""
Tic Tac Toe Player
"""

import math

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
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    #check which player makes the move
    current_player = player(board)
    #print(current_player)
    #check if action cell is not empty
    if (board[i][j]) != EMPTY:
        print("cell", i, j, "has been filled")
        #raise ValueError("Illegal Move")
    #change the cell with the symbol of the player
    else: 
        board[i][j] = current_player
    #print(board)
    #return the board with the change
    return board


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
    if terminal(board)==True:
        return None

    elif (current_player == X):
        max_action = (0,0)
        v = -9999
        for action in actions (board):
            if (v < min_value( result( board, action))): 
                # update v
                v = min_value( result( board, action))
                # update action
                max_action = action
        return max_action
    
    elif (current_player != X):
        min_action = (2,2)
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
    
    for action in actions(board):
        v = max(v, min_value( result(board, action)))
    print("value v:", v)
    return v

def min_value(board):
    """
    Return the lowest value of a set of result from actions
    """
    v = 9999

    for action in actions(board):
        v = min(v, max_value( result(board, action) ))
    print("value v:", v)
    return v