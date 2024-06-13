import pygame
import sys
import database
from Settings import * 

def main_menu(screen):
    title_font = pygame.font.Font(None, 150) 
    subtitle_font = pygame.font.Font(None, 50)
    menu_font = pygame.font.Font(None, 74)
    quit_font = pygame.font.Font(None, 36)

    while True:
        screen.fill(BLACK)
        title = title_font.render("KKK", True, RED)
        subtitle = subtitle_font.render("Kosmiczny Kurier Kombinant", True, WHITE)
        new_game_button = menu_font.render("Nowa Gra", True, GREEN)
        load_game_button = menu_font.render("Wczytaj Grę", True, GREEN)
        quit_button = quit_font.render("Wyjdź", True, RED)

        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 4 - 50))  # Tytuł przesunięty w górę
        subtitle_rect = subtitle.get_rect(center=(WIDTH // 2, HEIGHT // 4 + 25))  # Podtytuł bliżej tytułu
        new_game_rect = new_game_button.get_rect(center=(WIDTH // 2 - 150, HEIGHT // 2))  # Po lewej
        load_game_rect = load_game_button.get_rect(center=(WIDTH // 2 + 150, HEIGHT // 2))  # Po prawej
        quit_rect = quit_button.get_rect(bottomleft=(10, HEIGHT - 10))  # Lewy dolny róg

        screen.blit(title, title_rect)
        screen.blit(subtitle, subtitle_rect)
        screen.blit(new_game_button, new_game_rect)
        screen.blit(load_game_button, load_game_rect)
        screen.blit(quit_button, quit_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_rect.collidepoint(event.pos):
                    return "new_game"
                if load_game_rect.collidepoint(event.pos):
                    return "load_game"
                if quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

def hangar_menu(screen, day):
    menu_font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    while True:
        screen.fill(BLACK)
        title = menu_font.render(f"Hangar - Dzień {day}", True, WHITE)
        start_mission_button = small_font.render("Odpal Misję", True, GREEN)
        save_and_exit_button = small_font.render("Wyjdź z zapisem", True, RED)
        upgrades_button = small_font.render("Ulepszenia", True, GREEN)
        black_market_button = small_font.render("Czarny Rynek", True, GREEN)

        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        start_mission_rect = start_mission_button.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        upgrades_rect = upgrades_button.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        black_market_rect = black_market_button.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        save_and_exit_rect = save_and_exit_button.get_rect(bottomleft=(10, HEIGHT - 10))

        screen.blit(title, title_rect)
        screen.blit(start_mission_button, start_mission_rect)
        screen.blit(save_and_exit_button, save_and_exit_rect)
        screen.blit(upgrades_button, upgrades_rect)
        screen.blit(black_market_button, black_market_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_mission_rect.collidepoint(event.pos):
                    return "start_mission"
                if save_and_exit_rect.collidepoint(event.pos):
                    return "save_and_exit"
                if upgrades_rect.collidepoint(event.pos):
                    return "upgrades"
                if black_market_rect.collidepoint(event.pos):
                    return "black_market"

        pygame.display.flip()

def upgrade_menu(screen, player):
    small_font = pygame.font.Font(None, 36)
    while True:
        screen.fill(BLACK)
        rect_width, rect_height = 300, 100
        spacing = 20

        left_engine_rect = pygame.Rect(WIDTH // 4 - rect_width // 2, HEIGHT // 4 - rect_height // 2, rect_width, rect_height)
        right_engine_rect = pygame.Rect(3 * WIDTH // 4 - rect_width // 2, HEIGHT // 4 - rect_height // 2, rect_width, rect_height)
        engine_efficiency_rect = pygame.Rect(WIDTH // 2 - rect_width // 2, HEIGHT // 2 - rect_height // 2 + rect_height + spacing, rect_width, rect_height)
        engine_power_rect = pygame.Rect(WIDTH // 2 - rect_width // 2, HEIGHT // 2 - rect_height // 2 + 2 * (rect_height + spacing), rect_width, rect_height)

        quit_button = small_font.render("Wróć do hangaru", True, RED)
        quit_rect = quit_button.get_rect(bottomleft=(10, HEIGHT - 10))

        if not player.player_upgrades["Left_maneuvering_engine"]:
            color_left_engine = RED
        else:
            color_left_engine = GREEN

        if not player.player_upgrades["Right_maneuvering_engine"]:
            color_right_engine = RED
        else:
            color_right_engine = GREEN

        if not player.player_upgrades["Engine_efficiency"]:
            color_fuel_tank = RED
        else:
            color_fuel_tank = GREEN

        if not player.player_upgrades["Engine_power"]:
            color_main_engine = RED
        else:
            color_main_engine = GREEN

        pygame.draw.rect(screen, color_left_engine, left_engine_rect)
        pygame.draw.rect(screen, color_right_engine, right_engine_rect)
        pygame.draw.rect(screen, color_fuel_tank, engine_efficiency_rect)
        pygame.draw.rect(screen, color_main_engine, engine_power_rect)

        left_engine_label = small_font.render("Lewy Silnik Manewrowy", True, WHITE)
        right_engine_label = small_font.render("Prawy Silnik Manewrowy", True, WHITE)
        engine_efficiency_label = small_font.render("Efektywność Silnika", True, WHITE)
        engine_power_label = small_font.render("Moc Silnika", True, WHITE)

        screen.blit(left_engine_label, left_engine_label.get_rect(center=left_engine_rect.center))
        screen.blit(right_engine_label, right_engine_label.get_rect(center=right_engine_rect.center))
        screen.blit(engine_efficiency_label, engine_efficiency_label.get_rect(center=engine_efficiency_rect.center))
        screen.blit(engine_power_label, engine_power_label.get_rect(center=engine_power_rect.center))

        screen.blit(quit_button, quit_rect)

        money_label = small_font.render(f"Stan konta: {player.money} ¥", True, WHITE)
        money_rect = money_label.get_rect(topleft=(10, 10))
        screen.blit(money_label, money_rect)
        
        upgrade_cost_label = small_font.render(f"Koszt ulepszenia: {UPGRADE_COST} ¥", True, WHITE)
        upgrade_cost_rect = upgrade_cost_label.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10))
        screen.blit(upgrade_cost_label, upgrade_cost_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if left_engine_rect.collidepoint(event.pos) and not player.player_upgrades["Left_maneuvering_engine"]:
                    player.upgrade("Left_maneuvering_engine")
                if right_engine_rect.collidepoint(event.pos) and not player.player_upgrades["Right_maneuvering_engine"]:
                    player.upgrade("Right_maneuvering_engine")
                if engine_efficiency_rect.collidepoint(event.pos) and not player.player_upgrades["Engine_efficiency"]:
                    player.upgrade("Engine_efficiency")
                if engine_power_rect.collidepoint(event.pos) and not player.player_upgrades["Engine_power"]:
                    player.upgrade("Engine_power")
                if quit_rect.collidepoint(event.pos):
                    return "hangar_menu"

        pygame.display.flip()

def draw_text(screen, text, font, color, rect):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def save_game_menu(screen):
    pygame.init()
    font = pygame.font.Font(None, 36)
    slots = database.get_save_slots()
    screen.fill((0, 0, 0))

    slot_rects = []
    slot_width = 200
    slot_height = 100
    slot_margin = 50
    start_x = (screen.get_width() - (3 * slot_width + 2 * slot_margin)) // 2
    y = screen.get_height() // 2 - slot_height // 2

    for i in range(3):
        x = start_x + i * (slot_width + slot_margin)
        rect = pygame.Rect(x, y, slot_width, slot_height)
        slot_rects.append(rect)
        if i + 1 in slots:
            pygame.draw.rect(screen, (255, 0, 0), rect)
            draw_text(screen, f'Dzień {slots[i + 1]}', font, (255, 255, 255), rect)
        else:
            pygame.draw.rect(screen, (0, 255, 0), rect)
            draw_text(screen, 'Pusty', font, (255, 255, 255), rect)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(slot_rects):
                    if rect.collidepoint(event.pos):
                        return i + 1

def load_game_menu(screen):
    pygame.init()
    font = pygame.font.Font(None, 36)
    slots = database.get_save_slots()
    screen.fill((0, 0, 0))

    slot_rects = []
    slot_width = 200
    slot_height = 100
    slot_margin = 50
    start_x = (screen.get_width() - (3 * slot_width + 2 * slot_margin)) // 2
    y = screen.get_height() // 2 - slot_height // 2

    for i in range(3):
        x = start_x + i * (slot_width + slot_margin)
        rect = pygame.Rect(x, y, slot_width, slot_height)
        slot_rects.append(rect)
        if i + 1 in slots:
            pygame.draw.rect(screen, (255, 0, 0), rect)
            draw_text(screen, f'Dzień {slots[i + 1]}', font, (255, 255, 255), rect)
        else:
            pygame.draw.rect(screen, (0, 255, 0), rect)
            draw_text(screen, 'Pusty', font, (255, 255, 255), rect)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(slot_rects):
                    if rect.collidepoint(event.pos):
                        if i + 1 in slots:
                            return i + 1

    return None


def black_market_menu(screen, player):
    menu_font = pygame.font.Font(None, 74)
    fancy_font = pygame.font.Font(None, 60)
    small_font = pygame.font.Font(None, 36)
    
    # Load the cover image
    cover_image = pygame.image.load('Hermetic_book.png')
    
    while True:
        screen.fill(BLACK)
        title = menu_font.render("Czarny Rynek", True, WHITE)
        item_name = fancy_font.render("Wielka Księga Hermetycznej Wiedzy Tajemnej", True, GOLD)
        item_price = small_font.render("5000 ¥", True, GOLD)
        back_button = small_font.render("Wróć do Hangaru", True, RED)

        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 9))
        
        rect_width = 250
        rect_height = int(rect_width * 1.618)
        rect_x = WIDTH // 2 - rect_width // 2
        rect_y = HEIGHT // 1.75 - rect_height // 2
        
        pygame.draw.rect(screen, GOLD, (rect_x, rect_y, rect_width, rect_height))
        
        cover_rect = cover_image.get_rect(center=(rect_x + rect_width // 2, rect_y + rect_height // 2))
        
        screen.blit(cover_image, cover_rect)

        item_name_rect = item_name.get_rect(center=(WIDTH // 2, rect_y + 30))
        item_price_rect = item_price.get_rect(center=(WIDTH // 2, rect_y + rect_height - 30))
        back_button_rect = back_button.get_rect(bottomleft=(10, HEIGHT - 10))

        screen.blit(title, title_rect)
        screen.blit(item_name, item_name_rect)
        screen.blit(item_price, item_price_rect)
        screen.blit(back_button, back_button_rect)

        money_label = small_font.render(f"Stan konta: {player.money} ¥", True, WHITE)
        money_rect = money_label.get_rect(topleft=(10, 10))
        screen.blit(money_label, money_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    return "hangar_menu"

        pygame.display.flip()