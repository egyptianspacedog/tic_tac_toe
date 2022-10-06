"""
Tic Tac Toe Player
"""

import math, copy

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
    squareCount = {EMPTY: 0, X: 0, O: 0}

    # inspects each board element, incrementing the appropriate squareCount dict element
    for row in board:
        for column in row:
            squareCount[column] += 1
    # returns X if the board is empty, or if O was the last to take a turn
    if squareCount[EMPTY] == 9 or squareCount[X] == squareCount[O]:
        return X
    # otherwise, it's O's go
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    # inspects each grid coordinate, adding to the set if the space is empty
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                possibleActions.add((i, j))

    # only returns set if there is at least one possible move
    if len(possibleActions) > 0: 
        return possibleActions
    else:
        return None


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    playerChar = player(board)

    # uses deepcopy() method to make a true, "deep" clone, not just passing references
    newBoard = copy.deepcopy(board)

    # attempts to carry out the action, raising exception if the space isn't blank
    try:
        if board[action[0]][action[1]] == EMPTY:
            newBoard[action[0]][action[1]] = playerChar
            return newBoard
        else:
            raise Exception
    except:
        return None


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # alias for the sake of my fingers
    b = board

    # list to iterate over
    players = [X, O]

    # tedious way of checking for all 3-in-a-row patterns
    for player in players:
        for i in range(3):
            # horizontal checks
            if b[i][0] == b[i][1] == b[i][2] == player:
                return player
            # vertical checks
            if b[0][i] == b[1][i] == b[2][i] == player:
                return player
        # diagonal checks
        if b[0][0] == b[1][1] == b[2][2] == player:
            return player
        elif b[0][2] == b[1][1] == b[2][0] == player:
            return player
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # checks for winners or a full board
    if winner(board) != None or actions(board) == None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # ^^^
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
    if terminal(board):
        return None

    player_turn = player(board)
    best_move = None
    
    moves = actions(board)

    # variables to store highest and lowest overall scores. Set to inf/-inf to ensure first score is always better
    alpha = -math.inf
    beta = math.inf

    if player_turn == X:
        best_score = -math.inf
        # tries each action in turn, finding max score for that search path
        for action in moves:
            score = minimax_recursion(result(board, action), alpha, beta)
            if score > best_score:
                best_score = score
                best_move = action

    if player_turn == O:
        best_score = math.inf
        # same as above, but min
        for action in moves:
            score = minimax_recursion(result(board, action), alpha, beta)
            if score < best_score:
                best_score = score
                best_move = action
    return best_move
    
    
def minimax_recursion(board, alpha, beta):
    """
    Recursively searches all possible paths to terminal boards, evaluating the score of each in turn, then ultimately returning max/min score based on player
    """
    moves = actions(board)
    player_turn = player(board)

    if terminal(board):
        return minimax_util(board)

    if player_turn == X:
        max_score = -math.inf
        for action in moves:
            score = minimax_recursion(result(board, action), alpha, beta)
            max_score = max(score, max_score)
            alpha = max(alpha, score)
            # breaks when alpha exceeds beta, as min player will never allow a greater score
            if beta <= alpha:
                break
        return max_score
                
    else:
        min_score = math.inf
        for action in moves:
            score = minimax_recursion(result(board, action), alpha, beta)
            min_score = min(score, min_score)
            beta = min(beta, score)
            if alpha >= beta:
                break
        return min_score


def minimax_util(board):
    """ 
    counts no. of EMPTYs in current board - more EMPTYs suggesting strategy is more optimal - and returns count value +/- base board score
    """
    spaces = sum(n.count(EMPTY) for n in board)
    
    if winner(board) == X:
        return 1 + spaces

    elif winner(board) == O:
        return -1 - spaces
    else:
        return 0