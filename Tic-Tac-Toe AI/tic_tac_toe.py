""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                                                            SIMPLE TIC TAC TOE GAME                                                                                                          "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



import random

def create_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def find_winner(board, player):
    # Check row,column and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def player_move(board):
    while True:
        try:
            row = int(input("Enter the row value between 0,1 or 2:"))
            col = int(input("Enter the column value between 0,1 or 2:"))
            if board[row][col] == ' ':
                return row, col
            else:
                print("Cell already occupied \U0001f600. Try again.")
        except (ValueError, IndexError):
            print("Invalid input \U0001f636. Please enter valid row and column value.")

def computer_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def play_simple_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    new_var = "X"
    current_player = new_var

    while True:
        create_board(board)

        if current_player == "X":
            row, col = player_move(board)
        else:
            print("Computer's move:")
            row, col = computer_move(board)

        board[row][col] = current_player

        if find_winner(board, current_player):
            create_board(board)
            print(f"{current_player}-->User wins! \U0001f601")
            break

        if is_board_full(board):
            create_board(board)
            print("It's a tie!")
            break
        
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
            
if __name__ == "__main__":
    play_simple_tic_tac_toe()
