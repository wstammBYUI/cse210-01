"""
Assignment: Tic-Tac-Toe
Author: Stamm Walter 


"""

from doctest import ELLIPSIS_MARKER



def showBoard(board):
    for raw in board:
        for i in range(len(raw)):
            if i == len(raw) - 1:
                print(raw[i], end="\n")
            else:
                print(raw[i], end=" ")

def printBoard(board, position, player):
    answer='This place is already in use'
    if player:
        mark ="X"
    else:
        mark ="O"
    if position == 7:
        if board[4][0] == ' ':
            board[4][0] = mark
            return 0
        else:
            return answer
    elif position == 8:
        if board[4][2] == ' ':
            board[4][2] = mark
            return 0
        else:
            return answer
    elif position == 9:
        if board[4][4] == ' ':
            board[4][4] = mark
            return 0
        else:
            return answer
    elif position == 4:
        if board[2][0] == ' ':
            board[2][0] = mark
            return 0
        else:
            return answer
    elif position == 5:
        if board[2][2] == ' ':
            board[2][2] = mark
            return 0
        else:
            return answer
    elif position == 6:
        if board[2][4] == ' ':
            board[2][4] = mark
            return 0
        else:
            return answer
    elif position == 1:
        if board[0][0] == ' ':
            board[0][0] = mark
            return 0
        else:
            return answer
    elif position == 2:
        if board[0][2] == ' ':
            board[0][2] = mark
            return 0
        else:
            return answer
    elif position == 3:
        if board[0][4] == ' ':
            board[0][4] = mark
            return 0
        else:
            return answer
    else:
        return 'This place doesn´t exist'



def winner(board):
    for mark in ["X", "O"]:
        row0 = board[0][0] == mark and board[0][2] == mark and board[0][4] == mark
        row2 = board[2][0] == mark and board[2][2] == mark and board[2][4] == mark
        row4 = board[4][0] == mark and board[4][2] == mark and board[4][4] == mark
        column0 = board[0][0] == mark and board[2][0] == mark and board[4][0] == mark
        column2 = board[0][2] == mark and board[2][2] == mark and board[4][2] == mark
        column4 = board[0][4] == mark and board[2][4] == mark and board[4][4] == mark
        diagonallyUp = board[0][0] == mark and board[2][2] == mark and board[4][4] == mark
        diagonallyDown = board[4][0] == mark and board[2][2] == mark and board[0][4] == mark

        if row0 or row2 or row4 or column0 or column2 or column4 or diagonallyDown or diagonallyUp:
            if mark == 'X':
                return 1
            elif mark == 'O':
                return 2
            break


def main():

    board = [
        [' ', '|', ' ', '|', ' '],
        ['-', '+', '-', '+', '-'],
        [' ', '|', ' ', '|', ' '],
        ['-', '+', '-', '+', '-'],
        [' ', '|', ' ', '|', ' ']
    ]

    turnOne= True
    player_X= " PLAYER_X"
    player_O= "PLAYER_O"
    turn = 0

    showBoard(board)

    while turn < 9:
        if turnOne:
             print(f"{player_X}'s turn to choose a square (1-9): " )
        else:
            print(f"{player_O}'s turn to choose a square (1-9): " )
        play = int(input())

        sendValue= printBoard(board,play,turnOne)
        if sendValue ==0:
            turnOne = not turnOne
            turn += 1
            showBoard(board)
            if winner(board) ==1:
                print("PLAYER X won. Good game. Thanks for playing!")
                break
            elif winner(board) ==2:
                print("PLAYER O won. Good game. Thanks for playing!")
                break
        else:
            print(sendValue)
        if turn ==9:
            print("Tie")


if __name__ == "__main__":
    main()

