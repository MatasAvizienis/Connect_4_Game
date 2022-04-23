import numpy as np
import os

def game():
    num_of_rows = 6
    num_of_columns = 7

    board = np.zeros((num_of_rows,num_of_columns))
    possible_throws= ['1','2','3','4','5','6','7']

    # functions
    def throw(board, row, col, piece):
        board[row][col] = piece

    def is_there_free_row(board,col):
        return board[num_of_rows-1][col] == 0

    def available_row(board, col):
        for r in range(num_of_rows):
            if board[r][col]==0:
                return r

    def winning(board,piece):
        #horizontal 4
        for c in range(num_of_columns-3):
            for r in range(num_of_rows):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True
        # vertical 4
        for c in range(num_of_columns):
            for r in range(num_of_rows-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True
        # progressive diagonal win /
        for c in range(num_of_columns-3):
            for r in range(num_of_rows-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True


        # regressive diagonal win \
        for c in range(num_of_columns-3):
            for r in range(3,num_of_rows):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True

    def draw(board):
        if 0 not in board[5]:
            return True

    def display(board):
        line=''
        for row in board:
            for symbol in row:
                if symbol == 0:
                    line+='⚪'
                elif symbol == 1:
                    line+='🟡'
                elif symbol == 2:
                    line+='🔴'
        block = f"""
        {line[:7]}
        {line[7:14]}
        {line[14:21]}
        {line[21:28]}
        {line[28:35]}
        {line[35:42]}

        1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣
        """
        return block

    def clear():
        os.system('cls')

    def rematch():
        rematch = input("Norėdami žaisti dar kartą įrašykite 'taip':\n").lower()
        if rematch == 'taip':
            clear()
            game()
        else:
            print("Viso gero!")

    # Players names inputs
    player_1 = input(f"Įrašykite pirmojo žaidėjo vardą:\n")
    player_2 = input(f"Įrašykite antrojo žaidėjo vardą:\n")
    clear()

    # Printing empty board
    board_fliped = np.flip(board,0)
    print(display(board_fliped))


    game_over = False

    turn = 0
    while not game_over:
        # Player1 Player1 Player1 Player1 Player1 Player1 Player1 Player1 Player1 Player1 Player1 Player1 Player1 
        if turn == 0:
            col = input(f"🟡 {player_1} eilė. Įrašykite stulpelio numerį nuo 1 iki 7.\n")
            while col not in possible_throws:
                col = input(f"Pasirinktas stulpelis neegzistuoja. Įrašykite stulpelio numerį nuo 1 iki 7.\n")
            col=int(col)-1

            cheking = is_there_free_row(board,col)
            while cheking != True:
                col = input(f"🟡 {player_1} eilė. STULPELIS PILNAS. Įrašykite kitą stulpelio numerį nuo 1 iki 7.\n")
                while col not in possible_throws:
                    col = input(f"Pasirinktas stulpelis neegzistuoja. Įrašykite stulpelio numerį nuo 1 iki 7.\n")
                col=int(col)-1
                cheking = is_there_free_row(board,col)

            row = available_row(board,col)
            throw(board, row, col, 1)
            clear()
            print(display(board_fliped))
            
            if winning(board,1):
                print(f"🟡 {player_1} laimėjo!")
                game_over=True
                rematch()

            if draw(board):
                print("Lygiosios!")
                game_over=True
                rematch()
                    
            if not game_over:
                turn=1


        #Player2 Player2 Player2 Player2 Player2 Player2 Player2 Player2 Player2 Player2 Player2 Player2 Player2 
        if turn == 1:
            col = input(f"🔴 {player_2} eilė. Įrašykite stulpelio numerį nuo 1 iki 7.\n")
            while col not in possible_throws:
                col = input(f"Pasirinktas stulpelis neegzistuoja. Įrašykite stulpelio numerį nuo 1 iki 7.\n")
            col=int(col)-1

            cheking = is_there_free_row(board,col)
            while cheking != True:
                col = input(f"🔴 {player_2} eilė. STULPELIS PILNAS. Įrašykite kitą stulpelio numerį nuo 1 iki 7.\n")
                while col not in possible_throws:
                    col = input(f"Pasirinktas stulpelis neegzistuoja. Įrašykite stulpelio numerį nuo 1 iki 7.\n")
                col=int(col)-1
                cheking = is_there_free_row(board,col)

            row = available_row(board,col)
            throw(board, row, col, 2)
            clear()
            print(display(board_fliped))

            
            if winning(board,2):
                print(f"🔴 {player_2} laimėjo!")
                game_over=True
                rematch()

            if draw(board):
                print("Lygiosios!")
                game_over=True
                rematch()                    
            if not game_over:
                turn=0
game()