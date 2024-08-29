import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Run Function Once Example")

# Define the function you want to run once
def my_function():
    print("Function is called")
    return "Function result"

# Initialize the flag and the variable to store the result
function_called = False
result = None

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Run the function once and store the result
    if not function_called:
        result = my_function()
        function_called = True

    # Use the result in your game logic
    if result:
        print(f"Using the result: {result}")

    # Update the display
    screen.fill((0, 0, 0))
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
