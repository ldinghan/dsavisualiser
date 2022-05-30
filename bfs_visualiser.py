from collections import deque
import time

class Board:
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.board = []
		for i in range(self.row):
			tempRow = []
			for j in range(self.col):
				tempRow.append('.')
			self.board.append(tempRow)
		self.start = [0,0]
		self.end = [-1,-1]

	def chooseStart(self, position = [0,0]):
		self.board[position[0]][position[1]] = 'O'
		self.start = position


	def chooseEnd(self, position = [-1, -1]):
		self.board[position[0]][position[1]] = 'X'
		self.end = position

	def printBoard(self):
		for row in self.board:
			rowDisplay = ''
			for cell in row:
				rowDisplay += f'{cell} '
			print(rowDisplay)
		print('\n')

	def placeCounter(self, position):
		if self.board[position[0]][position[1]] == '.':
			self.board[position[0]][position[1]] = '+'



board = Board(10, 10)
board.chooseStart([3,4])
board.chooseEnd([5,7])
board.printBoard()


def isValid(visited, row, col):
	if (row < 0 or row >= board.row or col < 0 or col >= board.col):
		return False

	if (visited[row][col]):
		return False

	return True




def bfs(grid, row, col):
	q = deque()

	visited = [[False for i in range(board.col)] for i in range(board.row)]

	dRow = [ -1, 0, 1, 0]
	dCol = [ 0, 1, 0, -1]

	q.append((row, col, []))
	visited[row][col] = True

	while (len(q) > 0):
		time.sleep(0.2)
		cell = q.popleft()
		x = cell[0]
		y = cell[1]
		path = cell[2]
		path.append([x,y])
		if board.board[x][y] == 'X':
			print(f'found \nminimum distance: {len(path)} \nshortest path: {path}')
			return path
			break
		board.placeCounter([x,y])
		board.printBoard()

		for i in range(4):
			adjx = x + dRow[i]
			adjy = y + dCol[i]
			if (isValid(visited, adjx, adjy)):
				q.append((adjx, adjy, path[:]))
				visited[adjx][adjy] = True
#bfs(board.board, board.start[0], board.start[1])
	


path = bfs(board.board, board.start[0], board.start[1])
finalBoard = Board(board.row, board.col)
finalBoard.chooseStart(board.start)
finalBoard.chooseEnd(board.end)
for node in path:
	finalBoard.placeCounter(node)
	finalBoard.printBoard()

print(f'minimum distance: {len(path)} \nshortest path: {path}')