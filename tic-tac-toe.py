import random

# Tic-Tac-Toe board
board = [" " for _ in range(9)]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if the board is full
def is_full(board):
    return " " not in board

# Function to check if a player has won
def check_win(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to get a list of available moves
def available_moves(board):
    return [i for i, x in enumerate(board) if x == " "]

# Minimax function with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, "X"):
        return -1
    if check_win(board, "O"):
        return 1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = float("-inf")
        for move in available_moves(board):
            board[move] = "O"
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for move in available_moves(board):
            board[move] = "X"
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function to make the AI move
def ai_move(board):
    best_move = -1
    best_eval = float("-inf")
    alpha = float("-inf")
    beta = float("inf")

    for move in available_moves(board):
        board[move] = "O"
        eval = minimax(board, 0, False, alpha, beta)
        board[move] = " "
        if eval > best_eval:
            best_eval = eval
            best_move = move
        alpha = max(alpha, eval)

    board[best_move] = "O"

# Main game loop
while True:
    print_board(board)
    if is_full(board):
        print("It's a draw!")
        break

    player_move = -1  # Initialize player_move to -1

    while player_move < 0 or player_move >= 9 or board[player_move] != " ":
        try:
            player_move = int(input("Enter your move (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

    board[player_move] = "X"

    if check_win(board, "X"):
        print_board(board)
        print("You win!")
        break

    ai_move(board)

    if check_win(board, "O"):
        print_board(board)
        print("AI wins!")
        break
7