# tic_tac_toe
My implementation of an unbeatable Tic Tac Toe AI using the minimax algorithm, completed for CS50's AI course.

The base outline of the game - namely most things involving the actual pop-up window and "graphics" - were provided in the project shell.

The core of the task involved writing and creating the minimax algorithm, as well as several other functions (i.e. ones to evaluate board states).

The minimax algorithm involves two players being designated as either "min" or "max", with each being given a target score (i.e. -1 and 1, respectively). 
The given AI player then recursively loops through successive board states (moves) to see how the game could play out, with each final board state being
given a score based on who has won, or whether it was a draw (i.e. 0). The key principle of the algorithm is that for each turn it is 
assumed that turn's player will make their best move (go for whichever move leads to a score closest to their goal), as opposed to either AI player
assuming every move will work in their favour. As such, any given AI player (whether min or max) will ultimately choose moves that are the least damaging
based on this assumption. For this reason, the algorithm is unbeatable, with a human player only being able to achieve a draw at best.
