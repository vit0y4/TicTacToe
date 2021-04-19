'''
Abril 17
Autor: Vitoya
'''

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

boardKeys = []

for key in theBoard:
    boardKeys.append(key)

def printBoard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('------')

    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('------')

    print(board['1']+'|'+board['2']+'|'+board['3'])

#printBoard(theBoard)
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("Es el turno de la "+turn+" especifica el lugar donde quieres jugar")

        move= input()
        if move not in theBoard:
            print("Por favor escribe un numero del 1 al 9")
            continue

        if theBoard[move]==' ':
            theBoard[move]=turn
            count+=1
        else:
            print("Lo siento este lugar ya se encuentra ocupado, intenta con otro...")

            continue
        if count>=5:
            if theBoard['7']==theBoard['8']==theBoard['9']!=' ':
                printBoard(theBoard)
                print("El juego ha terminado")
                print("El jugador "+turn+ ", gana el juego")
                break
            if theBoard['4']==theBoard['5']==theBoard['6']!=' ':
                printBoard(theBoard)
                print("El juego ha terminado")
                print("El jugador "+turn+ ", gana el juego")
                break
            if theBoard['1']==theBoard['2']==theBoard['3']!=' ':
                printBoard(theBoard)
                print("El juego ha terminado")
                print("El jugador "+turn+ ", gana el juego")
                break
            if theBoard['7']==theBoard['5']==theBoard['3']!=' ':
                printBoard(theBoard)
                print("El juego ha terminado")
                print("El jugador "+turn+ ", gana el juego")
                break
            if theBoard['1']==theBoard['5']==theBoard['9']!=' ':
                printBoard(theBoard)
                print("El juego ha terminado")
                print("El jugador "+turn+ ", gana el juego")
                break
            if theBoard['7']==theBoard['4']==theBoard['1']!=' ':
                printBoard(theBoard)
                print("El juego ha terminado")
                print("El jugador "+turn+ ", gana el juego")
                break
            if theBoard['8']==theBoard['5']==theBoard['2']!=' ':
                printBoard(theBoard)
                print("El juego ha terminado")
                print("El jugador "+turn+ ", gana el juego")
                break
            if theBoard['9']==theBoard['6']==theBoard['3']!=' ':
                printBoard(theBoard)
                print("El juego ha terminado")
                print("El jugador "+turn+ ", gana el juego")
                break
        if count == 9:
            print("El juego ha terminado")
            print("Es un empate!!")

        if turn=="X":
            turn="O"
        else:
            turn="X"
    
    restart=input("Quieres volver a jugar? (Y/N)")
    if restart=='y' or restart=='Y':
        for key in boardKeys:
            theBoard[key]=' '
        game()



if __name__=="__main__":
    game()