import math

# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def is_winner(brd, player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(brd[i] == player for i in combo) for combo in win_combos)

def is_board_full(brd):
    return ' ' not in brd

def minimax(brd, depth, is_maximizing):
    if is_winner(brd, 'O'):
        return 1
    if is_winner(brd, 'X'):
        return -1
    if is_board_full(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                score = minimax(brd, depth + 1, False)
                brd[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                score = minimax(brd, depth + 1, True)
                brd[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

def play_game():
    print("Welcome to Tic Tac Toe! You are 'X' and the AI is 'O'.")
    print_board()

    while True:
        # Player move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move] != ' ':
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        board[move] = 'X'
        print_board()

        if is_winner(board, 'X'):
            print("You win!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        # AI move
        best_move()
        print("AI played:")
        print_board()

        if is_winner(board, 'O'):
            print("AI wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()