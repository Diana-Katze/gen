import pygame
import random
import sys

# Ініціалізація Pygame
pygame.init()

# Налаштування кольорів
BACKGROUND_COLOR = (240, 235, 220)  # Кавовий кремовий фон
SNAKE_COLOR = (0, 100, 0)           # Змійка темно-зелена
FOOD_COLOR = (255, 99, 71)           # Їжа томатна
BUTTON_COLOR = (100, 75, 55)       # Коричневий
BUTTON_HOVER_COLOR = (130, 100, 75)  # Світло коричневий
TEXT_COLOR = (60, 40, 30)         # Білий текст
LINE_COLOR = (150, 120, 90)           # Колір ліній

# Розміри екрану
WIDTH = 1000
HEIGHT = 600

# Налаштування екрану
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Змійка на Python')

# Швидкість кадрів
clock = pygame.time.Clock()

# Розмір блоку змійки та швидкість
SNAKE_BLOCK = 20
snake_speed = 12

# Шрифт для відображення тексту
font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 35)

# Функція для відображення очок
def show_score(score):
    value = score_font.render("Ваш рахунок: " + str(score), True, TEXT_COLOR)
    screen.blit(value, [10, 10])

# Функція для відображення змійки
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, SNAKE_COLOR, [x[0], x[1], snake_block, snake_block], border_radius=10)

# Функція для відображення їжі
def draw_food(x, y):
    pygame.draw.circle(screen, FOOD_COLOR, (x + SNAKE_BLOCK // 2, y + SNAKE_BLOCK // 2), SNAKE_BLOCK // 2)

# Функція для відображення повідомлення
def show_message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Функція для відображення кнопки
def draw_button(text, x, y, width, height):
    button_rect = pygame.Rect(x, y, width, height)
    mouse = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_rect, border_radius=10)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect, border_radius=10)

    label = font_style.render(text, True, TEXT_COLOR)
    screen.blit(label, (x + (width / 2 - label.get_width() / 2), y + (height / 2 - label.get_height() / 2)))

# Головна функція гри
def game_loop():
    game_over = False
    game_close = False

    # Початкове положення змійки
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Початкове положення їжі
    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(BACKGROUND_COLOR)
            show_message("Програв! Натисни Q для виходу або C для перезапуску", TEXT_COLOR)
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Обробка натискань клавіш
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x1_change == 0:
                        x1_change = -SNAKE_BLOCK
                        y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x1_change == 0:
                        x1_change = SNAKE_BLOCK
                        y1_change = 0
                elif event.key == pygame.K_UP:
                    if y1_change == 0:
                        y1_change = -SNAKE_BLOCK
                        x1_change = 0
                elif event.key == pygame.K_DOWN:
                    if y1_change == 0:
                        y1_change = SNAKE_BLOCK
                        x1_change = 0

        # Змійка виходить за межі екрану
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        # Оновлення позиції змійки
        x1 += x1_change
        y1 += y1_change
        screen.fill(BACKGROUND_COLOR)

        # Малювання їжі
        draw_food(foodx, foody)

        # Оновлення змійки
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Перевірка, чи зіткнулася змійка із собою
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Малювання змійки та рахунку
        draw_snake(SNAKE_BLOCK, snake_list)
        show_score(length_of_snake - 1)

        pygame.display.update()

        # Змійка з'їла їжу
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

# Вступна титульна сторінка
def main_menu():
    while True:
        screen.fill(BACKGROUND_COLOR)

        # Відображення вертикальних ліній по краях
        margin=10 # Відстань між лініями
        pygame.draw.line(screen, LINE_COLOR, (margin, 0), (margin, HEIGHT), 5)  # Ліва лінія
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - margin, 0), (WIDTH - margin, HEIGHT), 5)  # Права лінія
      

        # Відображення заголовку
        title = font_style.render("Гра 'Змійка'", True, TEXT_COLOR)
        screen.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 4))

        # Малювання змійки на титульній сторінці
        snake_list = [[WIDTH / 2, HEIGHT / 2 + 60], [WIDTH / 2 - SNAKE_BLOCK, HEIGHT / 2 + 60], [WIDTH / 2 - 2 * SNAKE_BLOCK, HEIGHT / 2 + 60]]
        draw_snake(SNAKE_BLOCK, snake_list)

        # Кнопка старт
        draw_button("Старт", WIDTH / 2 - 70, HEIGHT / 2 + 40, 140, 40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH / 2 - 70 <= event.pos[0] <= WIDTH / 2 + 70 and HEIGHT / 2 + 40 <= event.pos[1] <= HEIGHT / 2 + 80:
                    game_loop()

        pygame.display.update()

# Запуск гри
main_menu()
