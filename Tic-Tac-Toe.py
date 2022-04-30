from ast import Break, Try
import random
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
choices = ["X", "O"]
Player = ""
while Player not in choices:
    Player = input("O or X: ").upper()
Computer = ""
if Player == "O":
    Computer = "X"
else:
    Computer = "O"
    
winner = None
gameRunning = True

#-----------------------------------------------------------------------
# printing the game board
def printBoard(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]}")


#-----------------------------------------------------------------------
# take player input
def playerInput(board, positions):
    try:
        player = ""
        while player not in positions:
            player = int(input("Enter a number 1-9: "))
    except ValueError:
        print("Type a number, Idiot!")
        playerInput(board, positions)
        
    if player >= 1 and player <= 9 and board[player-1] == "-":
        board[player-1] = Player
        positions.remove(player)
        return True
    else:
        print("Oops spot already ocupied")
        return False
def computerTurn(positions, board):
    computer = random.choice(positions)
    positions.remove(computer)
    board[computer-1] = Computer
#-----------------------------------------------------------------------
# check for win and tie
def checkHorizontal(board, Player):
    if board[0] == board[1] == board[2] == Player and board[0] != "-":
        return True
        
    if board[3] == board[4] == board[5] == Player and board[3] != "-":
        return True
        
    if board[6] == board[7] == board[8] == Player and board[6] != "-":
        return True
        
    return False
        
def checkRow(board, Player):
    if board[0] == board[3] == board[6] == Player and board[0] != "-":
        return True
        
    if board[1] == board[4] == board[7] == Player and board[1] != "-":
        return True
        
    if board[2] == board[5] == board[8] == Player and board[2] != "-":
        return True
        
    return False

def checkDiag(board, Player):
    if board[0] == board[4] == board[8] == Player and board[0] != "-":
        return True
        
    if board[2] == board[4] == board[6] == Player and board[2] != "-":
        return True
        
    return False

def checkTie(board):
    if "-" not in board:
        return True

# switch the player

# check for win and tie
while gameRunning:
    printBoard(board)
    playerInput(board, positions)
    if checkHorizontal(board, Player):
        printBoard(board)
        print("You win!")
        break
    if checkHorizontal(board, Computer):
        printBoard(board)
        print("You lose!")
        break
    if checkRow(board, Player):
        printBoard(board)
        print("You win!")
        break
    if checkRow(board, Computer):
        printBoard(board)
        print("You lose!")
        break
    if checkDiag(board, Player):
        printBoard(board)
        print("You win!")
        break
    if checkDiag(board, Computer):
        printBoard(board)
        print("You lose!")
        break
    
    elif checkTie(board):
        printBoard(board)
        print("Tie!")
        break
    computerTurn(positions, board)