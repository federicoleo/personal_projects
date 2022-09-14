# Miglioramenti:
# Fare funzioni per ogni passaggio con lo switch del player

from itertools import product
#First the characters for the 2 players are initialized.
characterPosition1 = "| o"
characterPosition2 = "| x"

#Function to visualize the board in a more user-friendly way.
def visualize_board(columns, board):
        index_columns = [i+1 for i in range(columns)]
        print("  "+"   ".join(map(str, index_columns)))
        for i in board:
            print("+---"*(columns)+"+")
            print("|   "*columns+"|")
            print(" ".join(i)+" |")
            print("|   "*columns+"|")
        print("+---"*(columns)+"+")
        print("  "+"   ".join(map(str, index_columns)))

#Function to create the board that returns number of rows, columns and the 2d board.
def the_board():
    print("Num of rows:")
    row = int(input())
    print("Num of Cols:")
    columns = int(input())
    board = [["|  " for a in range(columns)] for b in range(row)]
    visualize_board(columns, board)

    return row, columns, board


################################################
#INTERACTING WITH THE BOARD

#Function that plays a complete game of Connect Four.
def drop_the_piece(rows, columns, board):
    full_columns = []
    all_columns = [column for column in range(columns)]
    tie=False
 

    #PLAYER1 LOOP
    while True:

        if tie:
            print("IT'S A TIE BOYS, GAME OVER")
            break

        print("PLAYER 1 -> Select the column of the piece:")
        characterY1 = int(input())-1
        
        if characterY1 < 0 or characterY1 > columns-1:
            print("NO! PLAYER 1 You are out of bounds, please re-select the column.")
            continue

        if characterY1 in full_columns:
            print("This column is already been filled! Please re-select it.")
            continue


        #PLAYER1 SELECTION
        for i in range(rows-1, -1, -1):
            if board[i][characterY1] == characterPosition1 or board[i][characterY1] == characterPosition2:
                continue
            board[i][characterY1] = characterPosition1
            if i == 0:
                full_columns.append(characterY1)
                tie = all(column in full_columns for column in all_columns)
            break

        visualize_board(columns, board)

        #PLAYER1 WINNER CHECK:
        p1_wins = False
        #Horizontal
        for i, j in product(range(rows), range(columns-3)):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == characterPosition1:
                p1_wins = True
                break
            else:
                continue

        #Vertical
        for j, i in product(range(columns), range(rows-1, 2, -1)):
            if board[i][j] == board[i-1][j] == board[i-2][j] == board[i-3][j] == characterPosition1:
                p1_wins = True
                break
            else:
                continue        

        #Diagonal-1
        for i, j in product(range(rows), range(columns)):
            try:
                if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == characterPosition1:
                    p1_wins = True
                    break
            except IndexError:
                pass
        
        #Diagonal-2
        for i, j in product(range(rows), range(columns)):
            try:
                if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == characterPosition1:
                    p1_wins = True
                    break
            except IndexError:
                pass         

        if p1_wins:
            print("PLAYER 1 ,YOU WON MOTHERFUCKER! HOORAY")
            break

        #PLAYER2 LOOP
        test = 0
        while True:
            if test == 1:
                break
            
            print("PLAYER 2 -> Select the column of the piece:")
            characterY2 = int(input()) - 1
            
            if characterY2 < 0 or characterY2 > columns-1:
                print("NO! PLAYER 2 You are out of bounds, please re-select the column.")
                continue

            if characterY2 in full_columns:
                print("This column is already been filled! Please re-select it.")
                continue
            


            #PLAYER2 SELECTION
            for i in range(rows-1, -1, -1):
                if board[i][characterY2] == characterPosition1 or board[i][characterY2] == characterPosition2:
                    continue
                board[i][characterY2] = characterPosition2
                if i == 0:
                    full_columns.append(characterY2)
                    tie = all(column in full_columns for column in all_columns)
                break
            test += 1
        
            visualize_board(columns, board)
    
            #PLAYER2 WINNER CHECK
            p2_wins = False
            #Horizontal
            for i, j in product(range(rows), range(columns-3)):    
                if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == characterPosition2:
                    p2_wins = True
                    break
                else:
                    continue
            
            #Vertical
            for j, i in product(range(columns), range(rows-1, 2, -1)):
                if board[i][j] == board[i-1][j] == board[i-2][j] == board[i-3][j] == characterPosition2:
                    p2_wins = True
                    break
                else:
                    continue

            #Diagonal-1
            for i, j in product(range(rows), range(columns)):
                try:            
                    if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == characterPosition2:
                        p2_wins = True
                        break
                except IndexError:
                    pass

            #Diagonal-2
            for i, j in product(range(rows), range(columns)):    
                try:
                    if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == characterPosition2:
                        p2_wins = True
                        break
                except IndexError:
                    pass
    
        if p2_wins:
            print("PLAYER 2 ,YOU WON MOTHERFUCKER! HOORAY")
            break


#GAME LOOP
while True:
    playground = the_board()
    rows, columns, board = playground[0], playground[1], playground[2]
    drop_the_piece(rows, columns, board)
    answer = str(input('Run again? (y/n): '))
    if answer not in ('y', 'n'):
        print("invalid input.")
        break
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break