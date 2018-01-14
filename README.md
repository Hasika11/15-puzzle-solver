QUESTION-
Consider a variant of the 15-puzzle, but with the following important change. Instead of sliding a
single tile from one cell into an empty cell, in this variant, either one, two, or three tiles may be slid
left, right, up or down in a single move. For example, for a puzzle in this configuration:
1 2 3 4
5 6 7 8
9 10 12
13 14 15 11

The goal is to find a short sequence of moves that restores the canonical configuration (on the left
above) given an initial board configuration. Write a program called solver16.py that finds a solution
to this problem efficiently using A* search. Your program should run on the command line like:
./solver16.py [input-board-filename]
where input-board-filename is a text file containing a board configuration in a format like:
1 2 3 4
5 6 7 8
9 0 10 12
13 14 15 11
where 0 indicates the empty position. The program can output whatever you’d like, except that the
last line of output should be a representation of the solution path you found, in this format:
[move-1] [move-2] ... [move-n]
where each move is encoded as a letter L, R, U, or D for left, right, up, or down, respectively, followed
by 1, 2, or 3 indicating the number of tiles to move, followed by a row or column number (indexed
beginning at 1). For instance, the six successors shown above would correspond to the following six
moves (with respect to the initial board state):
R13 R23 L13 D23 D13 U13

The goal of the puzzle is to find the shortest possible sequence of moves that restores the canonical configuration given an initial board configuration provided in a text file called "input.txt" by the user.

To run the code, type the following in the terminal after cloning the repo: python solver15.py input.txt

IMPLEMENTATION-

The state space is the physical configuration of the board that is always evolving due to the successor function in our code. It includes all the different states including already visited states.

The initial state:
It could be any configuration of the 15 puzzle for example,
[[0,3,6,13], [5,8,2,1], [9,12,15,4], [14,11,10,7]]

The goal state:
The final state that the board should reach that is,
[[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]

The successor function:
For the current state that will be explored, the successor function checks if this state is solvable using the permutation inversion function. If yes, then it checks if it has been visited, if not then it appends to the visited states and explores its child nodes. While exploring the child nodes, the heuristics are calculated. We used 2 heurisitcs:
1. Number of misplaced tiles/Hamming distance:
In number of misplaced tiles we check for the tiles that are not in its correct position: For the above initial state, h(number of misplaced tiles) = 13

2. Manhattan distance:
Manhattan distance is calculated using the formula distance = |x2 - x1| + |y2 - y1| To optimize the state space, we divided the Manhattan distance by 3 because 3 tiles can be moved at once.

Both heuristics are admissible because they never overestimate the cost of reaching the goal state.
We are using Manhattan distance as a heuristic instead of misplaced tiles because the heuristic value of Manhattan is greater than that of the heuristic of the misplaced tiles. Both are admissible but manhattan distance takes less time as compared to misplaced tiles.
The algorithm keeps track of the blank tile that moves up, down, right, or left
Limitation: The algorithm runs smoothly for 15 moves and takes more time for puzzle configuration of more than 15 moves
Solution: Linear conflict would optimise this limitation. When two tiles in the goal state are in the same row or column such that tile 1 is to the right of tile 2 and tile 2 is to the left of tile 1 and in the current state both these tiles are in the same column or row or diagonal, then we call it a linear conflict.
