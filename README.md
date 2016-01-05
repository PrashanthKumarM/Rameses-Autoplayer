# Rameses Game Autoplayer

Rameses is a two-player game that requires a board having an n × n grid and n*n pebbles. Initially the board starts empty and all pebbles are in a pile beside the board. Player 1 picks up a pebble and places it in any square of the grid. Player 2 then picks up a pebble from the pile, and places it in any open square (i.e. any square except the one selected by Player 1). Play continues back and forth, with each player picking up a pebble from the pile and placing it in any open square. A player loses the game as soon as they place a pebble that completes a row, a column, or one of the two diagonals of the board, and then the other player wins.

This code plays the game automatically with perfect play every time in extremely less time. It uses the concepts of logical search in Artificial Intelligence.

Feed the current status of the rameses board as a linear string of 'x' and '.'. For example:

x...x..x..

the next move will be given with the state of board after the move.

the program is to be run as below:

				$ python rameses.py <size of board> <current board state> <max time>

Max time is expected eventhough it will not be of much significance as time taken is always within a second.

Example:

				$ python rameses.py 3 .x......x 5

(Based on the problem statement in Assignment 2 of CSCI B-551 Elements of Artificial Intelligence by Professor David J Crandall, Indiana University, Bloomington)