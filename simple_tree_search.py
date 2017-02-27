from graphics import *
import random
import copy
# import time

grid = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,-1,0,0,0],[0,0,0,-1,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
goodMoves = [[20,-3,11,8,8,11,-3,20],[-3,-7,-4,1,1,-4,-7,-3],[11,-4,2,2,2,2,-4,11],[8,1,2,-3,-3,2,1,8],[8,1,2,-3,-3,2,1,8],[11,-4,2,2,2,2,-4,11],[-3,-7,-4,1,1,-4,-7,-3],[20,-3,11,8,8,11,-3,20]]

# goodMoves = []

maxDepth = 3
windowSize = 800
win = GraphWin('Floor', windowSize, windowSize)
win.setCoords(0.0, 0.0, 8.0, 8.0)
win.setBackground("tan")

def onBoard(x,y):
    if x < 0 or x > 7 or y < 0 or y > 7:
        return False
    return True

def checkFlipPieces(turn, x,y, board):
    turnNum = 0
    if turn == "white":
        turnNum = 1
    else:
        turnNum = -1
    #upper left diag
    for i in range(1, 8):
        if onBoard(x - i, y - i) is False or board[x - i][y - i] == 0:
            break
        if board[x - i][y - i] == turnNum:
            for diff in range(0, i):
                if board[x - diff][y - diff] == -turnNum:
                    return True
            break

    #upper right diag
    for i in range(1, 8):
        if onBoard(x + i, y - i) is False or board[x + i][y - i] == 0:
            break
        if board[x + i][y - i] == turnNum:
            for diff in range(0, i):
                if board[x + diff][y - diff] == -turnNum:
                    return True
            break

    #bottom right diag
    for i in range(1, 8):
        if onBoard(x + i, y + i) is False or board[x + i][y + i] == 0:
            break
        if board[x + i][y + i] == turnNum:
            for diff in range(0, i):
                if board[x + diff][y + diff] == -turnNum:
                    return True
            break

    #bottom left diag
    for i in range(1, 8):
        if onBoard(x - i, y + i) is False or board[x - i][y + i] == 0:
            break
        if board[x - i][y + i] == turnNum:
            for diff in range(0, i):
                if board[x - diff][y + diff] == -turnNum:
                    return True
            break

    #left current row
    for i in range(1, 8):
        if onBoard(x - i, y) is False or board[x - i][y] == 0:
            break
        if board[x-i][y] == turnNum:
            for diff in range(0, i):
                if board[x - diff][y] == -turnNum:
                    return True
            break

    #right current row
    for i in range(1, 8):
        if onBoard(x + i, y) is False or board[x + i][y] == 0:
            break
        if board[x+i][y] == turnNum:
            for diff in range(0, i):
                if board[x + diff][y] == -turnNum:
                    return True
            break

    #upper current column
    for j in range(1, 8):
        if onBoard(x, y - j) is False or board[x][y - j] == 0:
            break
        if board[x][y - j] == turnNum:
            for diff in range(0, j):
                if board[x][y - diff] == -turnNum:
                    return True
            break

    #lower current column
    for j in range(1, 8):
        if onBoard(x, y + j) is False or board[x][y + j] == 0:
            break
        if board[x][y + j] == turnNum:
            for diff in range(0, j):
                if board[x][y + diff] == -turnNum:
                    return True
            break

    return False

def addIntoLegalMoves(x,y,legalMoves, turn, board):
    for i in range(-1, 2):
        for j in range(-1,2):
            if i != 0 or j != 0:
                if onBoard(x + i, y + j):
                    if grid[x + i][y + j] == 0:
                        piecesFlipped = checkFlipPieces(turn, x+i, y+j, board)
                        coordinateStr = str(x + i) + str(y + j)
                        if piecesFlipped and coordinateStr not in legalMoves:
                            legalMoves.append(coordinateStr)

def flipPieces(turn, x,y, board):
    turnNum = 0
    if turn == "white":
        turnNum = 1
    else:
        turnNum = -1

    numChange = 0
    #upper left diag
    for i in range(1, 8):
        if onBoard(x - i, y - i) is False or board[x - i][y - i] == 0:
            break
        if board[x - i][y - i] == turnNum:
            for diff in range(0, i):
                board[x - diff][y - diff] = turnNum
            break

    #upper right diag
    for i in range(1, 8):
        if onBoard(x + i, y - i) is False or board[x + i][y - i] == 0:
            break
        if board[x + i][y - i] == turnNum:
            for diff in range(0, i):
                board[x + diff][y - diff] = turnNum
            break

    #bottom right diag
    for i in range(1, 8):
        if onBoard(x + i, y + i) is False or board[x + i][y + i] == 0:
            break
        if board[x + i][y + i] == turnNum:
            for diff in range(0, i):
                board[x + diff][y + diff] = turnNum
            break

    #bottom left diag
    for i in range(1, 8):
        if onBoard(x - i, y + i) is False or board[x - i][y + i] == 0:
            break
        if board[x - i][y + i] == turnNum:
            for diff in range(0, i):
                board[x - diff][y + diff] = turnNum
            break

    #left current row
    for i in range(1, 8):
        if onBoard(x - i, y) is False or board[x - i][y] == 0:
            break
        if board[x-i][y] == turnNum:
            for diff in range(0, i):
                board[x - diff][y] = turnNum
            break

    #right current row
    for i in range(1, 8):
        if onBoard(x + i, y) is False or board[x + i][y] == 0:
            break
        if board[x+i][y] == turnNum:
            for diff in range(0, i):
                board[x + diff][y] = turnNum
            break

    #upper current column
    for j in range(1, 8):
        if onBoard(x, y - j) is False or board[x][y - j] == 0:
            break
        if board[x][y - j] == turnNum:
            for diff in range(0, j):
                board[x][y - diff] = turnNum
            break

    #lower current column
    for j in range(1, 8):
        if onBoard(x, y + j) is False or board[x][y + j] == 0:
            break
        if board[x][y + j] == turnNum:
            for diff in range(0, j):
                board[x][y + diff] = turnNum
            break

def find_score(gamestate, turn):
    numPieces = 0
    for x in range(8):
        for y in range(8):
            if turn == "black":
                if gamestate[x][y] == -1:
                    numPieces += 1
            else:
                if gamestate[x][y] == 1:
                    numPieces += 1
    return numPieces

def find_good_score(gamestate):
    value = 0
    for x in range(8):
        for y in range(8):
            if gamestate[x][y] == -1:
                value += goodMoves[x][y]
    return value

def alphabeta(node, depth, alpha, beta, turn):
    if depth == 0:
        return find_good_score(node)

    legalWhiteMoves = []
    legalBlackMoves = []
    for x in range(0, 8):
        for y in range(0, 8):
            if turn == "white":
                if node[x][y] == -1:
                    addIntoLegalMoves(x,y,legalWhiteMoves, turn, node)
            else:
                if node[x][y] == 1:
                    addIntoLegalMoves(x,y,legalBlackMoves, turn, node)

    if len(legalWhiteMoves) == 0 and len(legalBlackMoves) == 0:
        return find_good_score(node)

    if len(legalWhiteMoves) == 0:
        v = float("-inf")
        for move in legalBlackMoves: #black's move
            child = copy.deepcopy(node)
            xCoord = int(move[0])
            yCoord = int(move[1])
            flipPieces(turn, xCoord, yCoord, child)
            v = max(v, alphabeta(child, depth-1, alpha, beta, "white"))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v
    else: #white's move
        v = float("inf")
        for move in legalWhiteMoves:
            child = copy.deepcopy(node)
            xCoord = int(move[0])
            yCoord = int(move[1])
            flipPieces(turn, xCoord, yCoord, child)
            v = min(v, alphabeta(child, depth-1, alpha, beta, "black"))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v

def alphabeta_helper(depth, legalMoves, turn):
    max = float("-inf")
    possibleMoves = []
    for move in legalMoves:
        copyGrid = copy.deepcopy(grid)
        xCoord = int(move[0])
        yCoord = int(move[1])
        flipPieces(turn, xCoord, yCoord, copyGrid)
        ret = alphabeta(copyGrid, depth - 1, float("-inf"),float("inf"),"white")
        if ret > max:
            possibleMoves = [move]
            max = ret
        elif ret == max:
            possibleMoves.append(move)
    return random.choice(possibleMoves)

def mini_max(currDepth, turn, gamestate):
    if currDepth == maxDepth:
        return find_score(gamestate,"black")
    else:
        legalWhiteMoves = []
        legalBlackMoves = []
        for x in range(0, 8):
            for y in range(0, 8):
                if turn == "white":
                    if gamestate[x][y] == -1:
                        addIntoLegalMoves(x,y,legalWhiteMoves, turn, gamestate)
                else:
                    if gamestate[x][y] == 1:
                        addIntoLegalMoves(x,y,legalBlackMoves, turn, gamestate)

        if len(legalWhiteMoves) == 0 and len(legalBlackMoves) == 0:
            return find_score(gamestate,"black")
        else:
            if len(legalBlackMoves) == 0: #white's turn
                v = float("inf")
                for move in legalWhiteMoves:
                    gamestateCopy = copy.deepcopy(gamestate)
                    xCoord = int(move[0])
                    yCoord = int(move[1])
                    flipPieces(turn, xCoord, yCoord, gamestateCopy)
                    v = min(v, mini_max(currDepth + 1, "black", gamestateCopy))
                return v
            else: #black's turn
                v = float("-inf")
                for move in legalBlackMoves:
                    gamestateCopy = copy.deepcopy(gamestate)
                    xCoord = int(move[0])
                    yCoord = int(move[1])
                    flipPieces(turn, xCoord, yCoord, gamestateCopy)
                    v = max(v,mini_max(currDepth + 1, "white", gamestateCopy))
                return v

def mini_max_helper(currDepth, legalMoves, turn):
    coordinate = ""
    maximum = float("-inf")
    for move in legalMoves:
        copyGrid = copy.deepcopy(grid)
        xCoord = int(move[0])
        yCoord = int(move[1])
        flipPieces(turn, xCoord, yCoord, copyGrid)
        ret = mini_max(currDepth + 1, "white", copyGrid)
        if ret > maximum:
            maximum = ret
            coordinate = move
    return coordinate

def chooseOneMoveAhead(legalMoves):
    coordinate = ""
    max = float("-inf")
    for move in legalMoves:
        copyGrid = copy.deepcopy(grid)
        xCoord = int(move[0])
        yCoord = int(move[1])
        flipPieces("white",xCoord,yCoord,copyGrid)
        ret = find_score(copyGrid, "white")
        if ret > max:
            max = ret
            coordinate = move
    return coordinate

def mobilityHeuristic(turn, myLegalMoves, board = grid):
    theirLegalMoves = []
    value = 0
    if(turn == "black"):
        for x in range(0, 8):
            for y in range(0, 8):
                    if board[x][y] == -1:
                        addIntoLegalMoves(x, y, theirLegalMoves, "white", board)
    else:
        for x in range(0, 8):
            for y in range(0, 8):
                    if board[x][y] == 1:
                        addIntoLegalMoves(x, y, theirLegalMoves, "black", board)

    if (len(myLegalMoves) + len(theirLegalMoves) != 0):
        value = 100 * (len(myLegalMoves) - len(theirLegalMoves)) / (len(myLegalMoves) + len(theirLegalMoves))
    else:
        value = 0
    return value

def fillGrid(x, y):
    if (grid[y][x] != 0):
        color = ""
        if(grid[y][x] == 1):
            color = "white"
        elif(grid[y][x] == -1):
            color = "black"
        square = Circle(Point(x+0.5,7-y+0.5), 0.45)

        square.draw(win)
        square.setFill(color)

def main(goodMovesGrid = goodMoves, idealDepth = maxDepth):
    turn = "black"
    noLegalMoves = 0
    # count = 0

    global maxDepth
    maxDepth = idealDepth

    global goodMoves
    goodMoves = goodMovesGrid

    global grid
    grid = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,-1,0,0,0],[0,0,0,-1,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

    movesTaken = []
    while (True):
        # time.sleep(30)
        # print(grid)

        for x in range(7):
            grid_vert = Line(Point(x+1, 0), Point(x+1, 8))
            grid_vert.draw(win)

        for y in range(7):
            grid_horz = Line(Point(0, y+1), Point(8, y+1))
            grid_horz.draw(win)

        for r in range(8):
            for c in range(8):
                fillGrid(r,c)

        legalWhiteMoves = []
        legalBlackMoves = []
        for x in range(0, 8):
            for y in range(0, 8):
                if turn == "white":
                    if grid[x][y] == -1:
                        addIntoLegalMoves(x,y,legalWhiteMoves, turn, grid)
                else:
                    if grid[x][y] == 1:
                        addIntoLegalMoves(x,y,legalBlackMoves, turn, grid)
        xCoord = 9
        yCoord = 9
        coordinate = str(xCoord) + str(yCoord)
        if len(legalWhiteMoves) == 0 and len(legalBlackMoves) == 0:
            noLegalMoves += 1
            if turn == "white":
                turn = "black"
            else:
                turn = "white"
            if noLegalMoves == 2:
                break
        else:
            # print(legalWhiteMoves)
            # print(legalBlackMoves)

            # Taking a random move available from the list of moves down below
            coordinate = ""
            if len(legalWhiteMoves) != 0:
                coordinate = ""
                while (coordinate not in legalWhiteMoves and coordinate not in legalBlackMoves):
                    xCoord = input(turn + " where would you like to put your x coordinate? ")
                    yCoord = input(turn + " where would you like to put your y coordinate? ")
                    coordinate = str(xCoord) + str(yCoord)

                # coordinate = (random.choice(legalWhiteMoves))
                # coordinate = legalWhiteMoves[0]
                # xCoord = int(coordinate[0])
                # yCoord = int(coordinate[1])
                # coordinate = chooseOneMoveAhead(legalWhiteMoves)
                # xCoord = int(coordinate[0])
                # yCoord = int(coordinate[1])
                # randomness = random.randint(0,1)
                # randomness = 0
                # if count <= 8:
                # 	randomness = 1
                # if randomness == 0:
                # 	max = -1000
                # 	for i in range(len(legalWhiteMoves)):
                # 		currCoord = legalWhiteMoves[i]
                # 		currX = int(currCoord[0])
                # 		currY = int(currCoord[1])
                # 		if goodMoves[currX][currY] > max:
                # 			max = goodMoves[currX][currY]
                # 			xCoord = currX
                # 			yCoord = currY
                # else:
                # 	coordinate = (random.choice(legalWhiteMoves))
                # 	xCoord = int(coordinate[0])
                # 	yCoord = int(coordinate[1])
            else:
                # coordinate = mini_max_helper(0, legalBlackMoves, turn)
                # print("Black Move: " + coordinate)
                coordinate = alphabeta_helper(maxDepth, legalBlackMoves, turn)
                # coordinate = (random.choice(legalBlackMoves))
                xCoord = int(coordinate[0])
                yCoord = int(coordinate[1])
                movesTaken.append(coordinate)

                # print("black move: " + str(xCoord) + str(yCoord))
            if (turn == "white"):
                grid[xCoord][yCoord] = 1
            else:
                grid[xCoord][yCoord] = -1
            noLegalMoves = 0
            flipPieces(turn, xCoord, yCoord, grid)

            if turn == "white":
                turn = "black"
            else:
                turn = "white"
            # count += 1

    numWhitePieces = 0
    numBlackPieces = 0
    didWhiteWin = False
    for x in range(8):
        for y in range(8):
            if grid[x][y] == 1:
                numWhitePieces += 1
            elif grid[x][y] == -1:
                numBlackPieces += 1
    if numBlackPieces > numWhitePieces:
        didWhiteWin = False
        print("black won")
    elif numBlackPieces == numWhitePieces:
        didWhiteWin = False
        print("tie")
    else:
        didWhiteWin = True
        print("white won")
    return didWhiteWin, movesTaken

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main(goodMoves, 3)