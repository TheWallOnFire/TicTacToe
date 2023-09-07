import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 10
BOARD_SIZE = 3
CELL_SIZE = WIDTH // BOARD_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')

# Create the game board
board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

# Initialize the current player
current_player = 'X'

# Initialize scores
scores = {'X': 0, 'O': 0}

# Function to draw the game board
def draw_board():
    window.fill(BLUE)
    
    # Draw vertical lines
    for x in range(1, BOARD_SIZE):
        pygame.draw.line(window, BLACK, (x * CELL_SIZE, 0), (x * CELL_SIZE, HEIGHT), LINE_WIDTH)
    
    # Draw horizontal lines
    for y in range(1, BOARD_SIZE):
        pygame.draw.line(window, BLACK, (0, y * CELL_SIZE), (WIDTH, y * CELL_SIZE), LINE_WIDTH)
    
    # Draw X and O symbols
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            symbol = board[x][y]
            if symbol == 'X':
                pygame.draw.line(window, BLACK, (x * CELL_SIZE + LINE_WIDTH, y * CELL_SIZE + LINE_WIDTH), ((x + 1) * CELL_SIZE - LINE_WIDTH, (y + 1) * CELL_SIZE - LINE_WIDTH), LINE_WIDTH)
                pygame.draw.line(window, BLACK, ((x + 1) * CELL_SIZE - LINE_WIDTH, y * CELL_SIZE + LINE_WIDTH), (x * CELL_SIZE + LINE_WIDTH, (y + 1) * CELL_SIZE - LINE_WIDTH), LINE_WIDTH)
            elif symbol == 'O':
                pygame.draw.circle(window, BLACK, ((x * CELL_SIZE) + CELL_SIZE // 2, (y * CELL_SIZE) + CELL_SIZE // 2), CELL_SIZE // 2 - LINE_WIDTH // 2, LINE_WIDTH)
    
# Function to handle a player's move
def handle_click(x, y):
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    
    # Check if the clicked cell is empty
    if board[col][row] is None:
        board[col][row] = current_player
        switch_player()

# Function to switch the current player
def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

# Function to check for a winner
def check_winner():
    # Check rows
    for row in range(BOARD_SIZE):
        if board[0][row] == board[1][row] == board[2][row] is not None:
            return board[0][row]
    
    # Check columns
    for col in range(BOARD_SIZE):
        if board[col][0] == board[col][1] == board[col][2] is not None:
            return board[col][0]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] is not None:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] is not None:
        return board[2][0]
    
    # No winner
    return None

# Function to reset the game
def reset_game():
    global board, current_player
    board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    current_player = 'X'

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                handle_click(*pygame.mouse.get_pos())
    draw_board()

    # Draw scores
    font = pygame.font.Font(None, 36)
    text = font.render(f"Player X: {scores['X']}    Player O: {scores['O']}", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    window.blit(text, text_rect)

    pygame.display.update()

    if check_winner() is not None:
        scores[check_winner()] += 1
        print(f"Player {check_winner()} wins!")
        pygame.time.wait(1000)  # Pause for 1 second
        reset_game()
    elif all(board[i][j] is not None for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):
        print("It's a draw!")
        pygame.time.wait(1000)  # Pause for 1 second
        reset_game()