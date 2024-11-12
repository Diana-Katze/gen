import pygame
import random
import sys

# Ініціалізація Pygame
pygame.init()

# Налаштування екрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Генератор випадкових чисел")

# Кольори

background_color = (240, 235, 220)  # Світло-кремовий
text_color = (60, 40, 30)           # Темно-коричневий
button_color = (100, 75, 55)        # Коричневий
button_hover_color = (130, 100, 75) # Світліший коричневий
border_color = (130, 100, 75)          # Темно-коричневий для рамки
line_color = (150, 120, 90)          # Світло-коричневий для ліній


# Налаштування шрифта
font_size = 100
font = pygame.font.Font(None, font_size)
button_font = pygame.font.Font(None, 40)

# Функція для генерації випадкового числа
def generate_random_number():
    return random.randint(1, 10000)

# Основний цикл програми
random_number = None  # Змінна для зберігання випадкового числа

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Перевірка на натискання миші
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            
            # Перевірка, чи натиснуто кнопку
            if button_rect.collidepoint(mouse_x, mouse_y):
                random_number = generate_random_number()

    # Заповнення фону
    screen.fill(background_color)

    # Відображення випадкового числа
    if random_number is not None:
        text = font.render(str(random_number), True, text_color)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))

        # Рамка навколо числа
        border_rect = text_rect.inflate(40, 20)
        pygame.draw.rect(screen, border_color, border_rect, border_radius=20)  # Округлена рамка
        screen.blit(text, text_rect)  # Текст

    # Налаштування кнопки
    button_text = button_font.render("Згенерувати число", True, text_color)
    button_rect = button_text.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
    
    # Зміна кольору кнопки при наведенні
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, button_hover_color, button_rect.inflate(20, 20), border_radius=10)
    else:
        pygame.draw.rect(screen, button_color, button_rect.inflate(20, 20), border_radius=10)
    
    # Відображення кнопки
    screen.blit(button_text, button_rect)

    # Додаткові графічні елементи (наприклад, заголовок)
    title_font = pygame.font.Font(None, 60)
    title_text = title_font.render("Генератор випадкових чисел", True, text_color)
    title_rect = title_text.get_rect(center=(screen_width // 2, 50))
    screen.blit(title_text, title_rect)

    # Технічні елементи: лінії
    pygame.draw.line(screen, line_color, (0, 150), (screen_width, 150), 5)  # Верхня лінія
    pygame.draw.line(screen, line_color, (0, 500), (screen_width, 500), 5)  # Нижня лінія

    # Оновлення екрану
    pygame.display.flip()

