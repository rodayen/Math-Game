import pygame
import sys
import random
# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Times Table Practice Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (4, 36, 107)
PEACH = (255, 190, 152)
HOVER_COLOR = (0, 200, 0)
CLICK_COLOR = (0, 150, 0)

# Set up font
font = pygame.font.Font(None, 36)

# Function to interpolate between two colors
def interpolate_color(color1, color2, factor):
    return tuple(int(color1[i] + (color2[i] - color1[i]) * factor) for i in range(3))

# Button class
class Button:
    def __init__(self, x, y, width, height, color, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = HOVER_COLOR
        self.click_color = CLICK_COLOR
        self.current_color = color
        self.text = text
        self.action = action
        self.hovering = False
        self.clicked = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.current_color, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.hovering = True
        else:
            self.hovering = False

    def transition_color(self):
        if self.clicked:
            self.current_color = interpolate_color(self.color, self.click_color, 0.5)
        elif self.hovering:
            self.current_color = interpolate_color(self.color, self.hover_color, 0.5)
        else:
            self.current_color = self.color

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
                if self.action:
                    self.action()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.clicked = False

# Define actions for buttons
def set_easy():
    start_game(1)

def set_medium():
    start_game(2)

def set_hard():
    start_game(3)

# Create buttons
easy_button = Button(300, 200, 200, 50, GREEN, "Easy", set_easy)
medium_button = Button(300, 300, 200, 50, GREEN, "Medium", set_medium)
hard_button = Button(300, 400, 200, 50, GREEN, "Hard", set_hard)

buttons = [easy_button, medium_button, hard_button]

# Game logic
def start_game(m):
    global game_started, current_problem, user_input, mode
    game_started = True
    current_problem = 0
    user_input = ""
    mode = int(m)

def num_select(mode):
    easy = random.choice(list(range(3, 10)))
    medium = random.choice(list(range(11, 100)))
    hard = random.choice(list(range(101, 1000)))
    if mode == 3:
        return hard    
    elif mode == 2:
        return medium
    else:
        return easy

# generates problems takes in difficulty level and number of problems to generaate into a matrix
class ProblemGenerator():
    
    def __init__(self) -> None:
        return None

    def question(self, mode):
        var1 = num_select(mode)
        var2 = num_select(mode)
        answer = var1 * var2
        return [var1, var2, answer]

    def question_list(self, mode, question_index) -> list:
        question_matrix = []
        for n in range(question_index): 
            q_listing = ProblemGenerator().question(mode)
            question_matrix.append(q_listing)
        return question_matrix
    
    

        


# Main loop
running = True
game_started = False
mode = int
current_problem = 0
score = 0
user_input = ""
clock = pygame.time.Clock()
FPS = 30
question_index = 3

loop_exit = 1


while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            for button in buttons:
                button.check_click(event)
        elif event.type == pygame.KEYDOWN and game_started:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                if str(problem_text[current_problem][2]) == user_input:
                    score += 1
                user_input = ""
                current_problem += 1
                
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

    mouse_pos = pygame.mouse.get_pos()
    for button in buttons:
        button.update(mouse_pos)
        button.transition_color()

    screen.fill(PEACH)
    if not game_started:
        for button in buttons:
            button.draw(screen)
    else:
        if current_problem < question_index: 
            if loop_exit == 1: 
                problem_text = ProblemGenerator().question_list(mode, question_index)
                loop_exit += 1
            problem_text = list(problem_text)
            problem = f"{problem_text[current_problem][0]} * {problem_text[current_problem][1]}"
            
            problem_surface = font.render(str(problem), True, BLACK)
            screen.blit(problem_surface, (100, 100))

            input_surface = font.render(user_input, True, BLACK)
            screen.blit(input_surface, (100, 200))
        else:
            score_text = f"Your score is: {score}"
            score_surface = font.render(score_text, True, BLACK)
            screen.blit(score_surface, (100, 100))

    pygame.display.flip()



pygame.quit()
sys.exit()
