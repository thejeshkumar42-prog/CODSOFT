import random

board = [" " for i in range(9)]

def show_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for position in win_positions:
        if board[position[0]] == board[position[1]] == board[position[2]] == player:
            return True

    return False

def player_move():
    while True:
        move = int(input("Enter position (1-9): ")) - 1

        if board[move] == " ":
            board[move] = "X"
            break
        else:
            print("Position already taken. Try again.")

def computer_move():
    empty_positions = []

    for i in range(9):
        if board[i] == " ":
            empty_positions.append(i)

    move = random.choice(empty_positions)
    board[move] = "O"

def is_board_full():
    return " " not in board

print("=== TIC TAC TOE ===")
print("You are X")
print("Computer is O")

show_board()

while True:

    player_move()
    show_board()

    if check_winner("X"):
        print("Congratulations! You win!")
        break

    if is_board_full():
        print("It's a draw!")
        break

    print("Computer's turn...")
    computer_move()
    show_board()

    if check_winner("O"):
        print("Computer wins!")
        break

    if is_board_full():
        print("It's a draw!")
        break12