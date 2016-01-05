import sys

#	The following is the gameplay for rameses
#	with the current state of the board we determine the available spaces
#	we take these as tuples of rows and columns values
#	we place the pebble at that position where we can't complete a row, column or diagonal
#	I really did not bother about the time because for a 
#	20x20 rameses board it takes about 0.00369205665588 seconds

def main(n, board_string, time):
	board = process(board_string, n)
	print "Nice Move. Please wait while I think...."
	available_spaces = find_spaces(board)
	new_board = win_rameses(available_spaces, board, n)
	print "".join([val for sublist in new_board for val in sublist])

def process(board_string, n):
	board_string = list(board_string)
	return [board_string[i:i + n] for i in range(0, len(board_string), n)]

def find_spaces(board):
	available_spaces = {"row":[],"column":[]}
	for i in range(0,len(board)):
		for j in range(0,len(board[i])):
			if board[i][j] == ".":
				available_spaces["row"].append(i)
				available_spaces["column"].append(j)
	return available_spaces

def win_rameses(available_spaces, board, n):
	for i in [x for x,k in enumerate(available_spaces["row"]) if available_spaces["row"].count(k) >= 2]:
		row = available_spaces["row"][i]
		column = available_spaces["column"][i]
		if check_diagonals(board, [row, column], n) and check_column(board, [row, column], n):
			print "I would recommend you to place to pebble at Row "+str(row+1)+" Column "+str(column+1)
			print "New Board: "
			board[row][column] = "x"
			return board
	print "No more possible moves. Game Lost"
	return board

def check_diagonals(board, tup, n):
	right = left = False
	for i in range(0,n-1):
		j = n-1-i
		if [i,i] != tup and board[i][i] == ".":
			right = True
		if [i,j] != tup and board[i][j] == ".":
			left = True
	return right and left

def check_column(board, tup, n):
	for i in range(0,n-1):
		if [i,tup[1]] != tup and board[i][tup[1]] == ".":
			return True

if __name__ == "__main__": main(int(sys.argv[1]),sys.argv[2],int(sys.argv[3]))