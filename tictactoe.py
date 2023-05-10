
import random

# =============================================================================== DEFINE FUNCTIONS AND INITIAL VALUES

board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

# CLEAR SCREEN


def clear_output():
    print("\n"*100)

# CLEAR BOARD


def clear_board():
    for row in board:
        for i in range(len(row)):
            row[i] = "_"

# PLAYER 1 CHOOSE MARKER


def player_input():
    acceptable_values = ["X", "O"]
    marker = input("Player 1, choose X or O: ").upper()
    while marker not in acceptable_values:
        marker = input("Invalid input. Choose X or O: ").upper()
    return marker

# RANDOMIZE PLAYER'S SELECTION


def choose_first():
    flip = random.randint(1, 2)
    if flip == 1:
        return "Player 1 goes first"
    else:
        return "Player 2 goes first"

# DISPLAY BOARD


def display_board(board):
    for row in board:
        print("|".join(row))

# PLACE X/O MARKER ON BOARD


def place_marker(board, marker, position):
    if position <= 3:
        board[2][position-1] = marker
    elif position <= 6:
        board[1][position-4] = marker
    elif position <= 9:
        board[0][position-7] = marker

# CHECK FOR WINNING


def win_check(board, mark):
    for i in range(3):  # ROWS AND COLUMNS
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
    if board[0][0] == board[1][1] == board[2][2] == mark:  # DIAGONALS
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:  # DIAGONALS
        return True
    return False

# CHECK IF POSITION IS AVAILABLE


def space_check(board, position):
    if position <= 3:
        return board[2][position-1] == '_'
    elif position <= 6:
        return board[1][position-4] == '_'
    elif position <= 9:
        return board[0][position-7] == '_'

# CHECK IF BOARD IS FULL


def full_board_check(board):
    if "_" in board[0] or "_" in board[1] or "_" in board[2]:
        return False
    else:
        return True

# CHOOSE PLAYER'S POSITION FUNCTION


def player_choice(board, marker):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input(f"{marker} - choose a position: (1-9)"))
        if position not in range(1, 10):
            print("Out of range")
        elif not space_check(board, position):
            print("Position already taken!")

    return position

# CHECK REPLAY FUNCTION


def replay():
    print("Do you want to play again? (yes/no)")
    return input().lower().startswith("y")

# =============================================================================== DEFINE HELPER FUNCTIONS


def update_ui(board):  # Update the UI with the latest board state
    clear_output()
    display_board(board)


def win_tie_check(board, marker):  # Win/Tie check helper function
    if win_check(board, marker):
        print(f"{marker} wins!")
        return True
    elif full_board_check(board):
        print("It's a tie!")
        return True
    return False


# =============================================================================== EXECUTE GAME LOGIC
while True:
    # INITIAL SETUP
    print('Welcome to Tic Tac Toe!')

    first = choose_first()

    if first == "Player 1 goes first":
        player1_marker = player_input()
        player2_marker = "O" if player1_marker == "X" else "X"
        print(first)
    else:
        player2_marker = player_input()
        player1_marker = "O" if player2_marker == "X" else "X"
        print(first)

    display_board(board)

    # GAMEPLAY
    while not full_board_check(board):

        # PLAYER 1 TURN
        player1 = player_choice(board, player1_marker)
        place_marker(board, player1_marker, player1)
        update_ui(board)
        if win_tie_check(board, player1_marker):
            break

        # PLAYER 2 TURN
        player2 = player_choice(board, player2_marker)
        place_marker(board, player2_marker, player2)
        update_ui(board)
        if win_tie_check(board, player2_marker):
            break
    # CHECK IF PLAYER WANTS TO PLAY AGAIN
    if not replay():
        break
