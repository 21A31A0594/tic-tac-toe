board=["-","-","-",
       "-","-","-",
       "-","-","-"]
currentplayer="X"
winner=None
gamerunning = True
def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])
def playerinput(board):
    while True:
        if currentplayer == "X":
            inp = int(input(f"Enter a number 1-9: "))
        else:
            inp = int(input(f"Enter a number 1-9: "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-":
            board[inp-1] = currentplayer
            break
        else:

            if currentplayer == "X":
                print(f"Oops! Try again! Player")
            else:
                print(f"Oops! Try again! Player")
            printboard(board)
def checkhorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = currentplayer
        return True
def checkrow(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = currentplayer
        return True
def checkdiagonal(board):
    global winner
    if (board[0] == board[4] == board[5] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentplayer
        return True
def checktie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("Its a tie")
        gamerunning = False

def checkwin():
    if checkdiagonal(board) or checkhorizontal(board) or checkrow(board):
        print(f"The winner is {winner}")
def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"
while gamerunning:
    printboard(board)
    if winner != None:
        break
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer()

