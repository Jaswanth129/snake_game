import random
import pygame

# Initialize
pygame.init()

# Screen setup
width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grishma Snake Game")

# Snake settings
snake_x, snake_y = width // 2, height // 2
change_x, change_y = 0, 0
snake_body = [(snake_x, snake_y)]
snake_size = 10

# Food position
food_x = random.randrange(0, width, snake_size)
food_y = random.randrange(0, height, snake_size)

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    game_screen.fill((150, 150, 150))

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and change_x == 0:
                change_x = -snake_size
                change_y = 0
            elif event.key == pygame.K_RIGHT and change_x == 0:
                change_x = snake_size
                change_y = 0
            elif event.key == pygame.K_UP and change_y == 0:
                change_x = 0
                change_y = -snake_size
            elif event.key == pygame.K_DOWN and change_y == 0:
                change_x = 0
                change_y = snake_size

    # Move snake
    snake_x = (snake_x + change_x) % width
    snake_y = (snake_y + change_y) % height
    new_head = (snake_x, snake_y)

    # Game Over if snake bites itself
    if new_head in snake_body[1:]:
        print("GAME OVER")
        pygame.quit()
        quit()

    snake_body.append(new_head)

    # Check food collision
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randrange(0, width, snake_size)
        food_y = random.randrange(0, height, snake_size)
    else:
        snake_body.pop(0)

    # Draw food
    pygame.draw.circle(game_screen, (0, 0, 128), (food_x, food_y), 6)

    # Draw snake
    for (x, y) in snake_body:
        pygame.draw.circle(game_screen, (255, 255, 102), (x, y), 6)

    pygame.display.update()
    clock.tick(15)

pygame.quit()
