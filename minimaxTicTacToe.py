# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 22:32:55 2021

@author: fatih
"""

def tablo(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


def bosluk(pozisyon):
    if board[pozisyon] == ' ':
        return True
    else:
        return False


def hücregir(harf, pozisyon):
    if bosluk(pozisyon):
        board[pozisyon] = harf
        tablo(board)
        if (beraberlik()):
            print("Beraberlik!")
            exit()
        if winkontrol():
            if harf == 'X':
                print("AI kazandı!")
                exit()
            else:
                print("Sen Kazandın(bunu yapabilirsen beni bul)!")
                exit()

        return


    else:
        print("Bu hücre dolu!")
        pozisyon = int(input("Lütfen yeni bir hücre gir:  "))
        hücregir(harf, pozisyon)
        return


def winkontrol():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def kimkazandı(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def beraberlik():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def oyuncuhareketi():
    pozisyon = int(input("'O' için hücre gir:  "))
    hücregir(player, pozisyon)
    return


def comphareketi():
    bestScore = -1000
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    hücregir(bot, bestMove)
    return


def minimax(board, derinlik, isMaximizing):
    if (kimkazandı(bot)):
        return 1
    elif (kimkazandı(player)):
        return -1
    elif (beraberlik()):
        return 0

    if (isMaximizing):
        bestScore = -1000
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, derinlik + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, derinlik + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

tablo(board)
print("Bilgisayar başlar, İyi Şanslar.")
print("Hücreler aşağıdaki gibi:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'
bot = 'X'


global firstComputerMove
firstComputerMove = True

while not winkontrol():
    comphareketi()
    oyuncuhareketi()
