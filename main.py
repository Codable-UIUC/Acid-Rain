import pygame
import random
import os
import sys
from button import Button
from pygame import mixer

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (128, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Acid Rain")
clock = pygame.time.Clock()

BG = pygame.image.load("rain.png")

mixer.music.load('bgm.wav')
mixer.music.play(-1)


def get_font(size): 
    return pygame.font.Font("font.ttf", size)

def play():
    dictionary = [  "abaca", "agars", "based", "beget", "cease",
                    "cared", "dwarf", "draws", "eager", "eased",
                    "favas", "fewer", "gears", "geste", "refed",
                    "rewed", "sabed", "scabs", "swarf", "tates",    # Easy
                    "attest", "averts", "bardes", "bazars", "carafe", 
                    "decare", "deface", "estate", "evaded", "facade", 
                    "fatwas", "fessed", "grater", "rabats", "ragbag",
                    "scatts", "screws", "tasset", "wagger", "xebecs",   # Meduim
                    "abraders", "asserter", "beverage", "braggers", "catawbas",
                    "debaters", "degasses", "effected", "egresses", "feedbags", 
                    "gabfests", "grabbers", "refracts", "reverter", "scarcest",
                    "serrates", "tattered", "warcraft", "wattages", "zareebas", # Hard
                    "aftereffect", "asseverates", "beggarweeds", "crabgrasses", "decerebrate",
                    "desegregate", "effervesced", "effervesces", "exacerbates", "exaggerated",
                    "extravagate", "readdressed", "reaggregate", "resegregate", "revegetated",
                    "sassafrases", "stagecrafts", "stavesacres", "tradecrafts", "wastewaters"   # Extreme
                ]
    #(index 0~19): Easy (index 20~39): Medium (index 40~59): Hard (index 60~79): Extreme
    rand_1 = True
    rand_2 = True
    rand_3 = True
    rand_4 = True
    rand_5 = True
    level = 0
    level_clear = False
    miss = 0
    gameOver = False
    word_count = 0
    user_text = ''
    input_rect = pygame.Rect(450, 660, 120, 30)
    color_active = pygame.Color('lightskyblue')
    color_passive = pygame.Color('blue')
    color = color_passive
    active = False
    w1 = 0
    w2 = 0
    w3 = 0
    w4 = 0
    w5 = 0

    while True:
        clock.tick(30)

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(WHITE)

        # PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        myFont = pygame.font.SysFont("arial", 20, False, True)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
        if active:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(SCREEN, color, input_rect)
        text_surface = myFont.render(user_text, True, BLACK)
        SCREEN.blit(text_surface, (input_rect.x+5, input_rect.y+5))

        print(user_text)    # to cheack input

        input_rect.w = max(100, text_surface.get_width()+10)
        
        if rand_1 == True:
            w1 = dictionary[random.randrange(10*level, 20+10*level)]
            word_1 = myFont.render(w1, True, BLACK)
            #   level 0: randrange(0, 20)   level 1: randrange(10, 30)  level 2: randrange(20, 40)
            #   level 3: randrange(30, 50)   level 4: randrange(40, 60)   level 5: randrange(50, 70)
            #   level 6: randrange(60, 79)
            #   randrange(10*level, 20+10*level) level start with 0
            text_Rect = word_1.get_rect()
            text_Rect.x = 10
            text_Rect.y = 10
            word_1_x = random.randrange(0, 150)
            word_1_y = 0
            speed_1 = random.randrange(1+level, 4+level)
            rand_1 = False
        
        if rand_2 == True:
            w2 = dictionary[random.randrange(10*level, 20+10*level)]
            word_2 = myFont.render(w2, True, BLACK)
            text_Rect = word_2.get_rect()
            text_Rect.x = 10
            text_Rect.y = 10
            word_2_x = random.randrange(200, 350)
            word_2_y = 0
            speed_2 = random.randrange(1+level, 4+level)
            rand_2 = False

        if rand_3 == True:
            w3 = dictionary[random.randrange(10*level, 20+10*level)]
            word_3 = myFont.render(w3, True, BLACK)
            text_Rect = word_3.get_rect()
            text_Rect.x = 10
            text_Rect.y = 10
            word_3_x = random.randrange(400, 550)
            word_3_y = 0
            speed_3 = random.randrange(1+level, 4+level)
            rand_3 = False

        if rand_4 == True:
            w4 = dictionary[random.randrange(10*level, 20+10*level)]
            word_4 = myFont.render(w4, True, BLACK)
            text_Rect = word_4.get_rect()
            text_Rect.x = 10
            text_Rect.y = 10
            word_4_x = random.randrange(600, 750)
            word_4_y = 0
            speed_4 = random.randrange(1+level, 4+level)
            rand_4 = False

        if rand_5 == True:
            w5 = dictionary[random.randrange(10*level, 20+10*level)]
            word_5 = myFont.render(w5, True, BLACK)
            text_Rect = word_5.get_rect()
            text_Rect.x = 10
            text_Rect.y = 10
            word_5_x = random.randrange(800, 950)
            word_5_y = 0
            speed_5 = random.randrange(1+level, 4+level)
            rand_5 = False

        SCREEN.blit(word_1, (word_1_x, word_1_y))
        SCREEN.blit(word_2, (word_2_x, word_2_y))
        SCREEN.blit(word_3, (word_3_x, word_3_y))
        SCREEN.blit(word_4, (word_4_x, word_4_y))
        SCREEN.blit(word_5, (word_5_x, word_5_y))
        
        word_1_y += speed_1
        word_2_y += speed_2
        word_3_y += speed_3
        word_4_y += speed_4
        word_5_y += speed_5

        if user_text == w1:
            rand_1 = True
            word_count += 1
            user_text = ''
        if user_text == w2:
            rand_2 = True
            word_count += 1
            user_text = ''
        if user_text == w3:
            rand_3 = True
            word_count += 1
            user_text = ''
        if user_text == w4:
            rand_4 = True
            word_count += 1
            user_text = ''
        if user_text == w5:
            rand_5 = True
            word_count += 1
            user_text = ''

        if word_1_y >= 620:
            rand_1 = True
            miss += 1
        if word_2_y >= 620:
            rand_2 = True
            miss += 1
        if word_3_y >= 620:
            rand_3 = True
            miss += 1
        if word_4_y >= 620:
            rand_4 = True
            miss += 1
        if word_5_y >= 620:
            rand_5 = True
            miss += 1

        if level_clear == True:
            level += 1
            miss = 0
            level_clear = False

        if word_count % 20 == 19:
            level_clear = True

        if (word_count == 2):
            gameOver = True
        
        if gameOver == True:
            break

        myFont = pygame.font.SysFont("arial", 20, True, True)
        level_Title = myFont.render("LEVEL: ", True, BLACK)
        level_Rect = level_Title.get_rect()
        level_Rect.x = 1100
        level_Rect.y = 10
        SCREEN.blit(level_Title, level_Rect)

        level_Title2 = myFont.render(str((level)), True, BLACK)
        level_Rect2 = level_Title2.get_rect()
        level_Rect2.x = 1200
        level_Rect2.y = 10
        SCREEN.blit(level_Title2, level_Rect2)

        word_Title = myFont.render("Word Count: ", True, BLACK)
        level_Rect = word_Title.get_rect()
        level_Rect.x = 1100
        level_Rect.y = 35
        SCREEN.blit(word_Title, level_Rect)

        word_Title2 = myFont.render(str((word_count)), True, BLACK)
        level_Rect2 = word_Title2.get_rect()
        level_Rect2.x = 1250
        level_Rect2.y = 35
        SCREEN.blit(word_Title2, level_Rect2)

        pygame.display.update()
    
    myFont_1 = pygame.font.SysFont("arial", 50, True, True)
    endText = myFont_1.render("GAME OVER",True, RED)
    endText_rect = endText.get_rect()
    endText_rect.center = (640, 100) 

    endText1 = myFont_1.render("Total Word Count: "+str((word_count))+"", True, GREEN)
    endText1_rect = endText1.get_rect()
    endText1_rect.center = (640, 150)

    endText2 = myFont_1.render("Press ESC to Quit", True, BLUE)
    endText2_rect = endText2.get_rect()
    endText2_rect.center = (640, 200)

    while gameOver:
        SCREEN.blit(endText, endText_rect)
        SCREEN.blit(endText1, endText1_rect)
        SCREEN.blit(endText2, endText2_rect)
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_menu()
    
def options():
    while True:
        
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0,0))

        ##OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        ##OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        ##SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        ##OPTIONS_CHARACTER = Button(image=pygame.image.load("button.png"), pos=(640, 250), 
                            ##text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        OPTIONS_ON = Button(image=pygame.image.load("button.png"), pos=(640, 100), 
                            text_input="BGM ON", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_OFF = Button(image=pygame.image.load("button.png"), pos=(640, 250), 
                            text_input="BGM OFF", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_CREDITS = Button(image=pygame.image.load("button.png"), pos=(640, 400), 
                            text_input="CREDITS", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_BACK = Button(image=pygame.image.load("button.png"), pos=(640, 600), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_ON.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_ON.update(SCREEN)
        OPTIONS_OFF.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_OFF.update(SCREEN)
        OPTIONS_CREDITS.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_CREDITS.update(SCREEN)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_ON.checkForInput(OPTIONS_MOUSE_POS):
                    mixer.music.play(-1)
                if OPTIONS_OFF.checkForInput(OPTIONS_MOUSE_POS):
                    mixer.music.stop()
                if OPTIONS_CREDITS.checkForInput(OPTIONS_MOUSE_POS):
                    credits()
        pygame.display.update()
        


def credits():
    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        CREDITS_TEXT = get_font(40).render("CREDITS TO:", True, "Yellow")
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)
        CREDITS_TEXT1 = get_font(30).render("Joon Song, Jasmine Song", True, "Yellow")
        CREDITS_RECT1 = CREDITS_TEXT.get_rect(center=(350, 200))
        SCREEN.blit(CREDITS_TEXT1, CREDITS_RECT1)
        CREDITS_TEXT2 = get_font(30).render("YunSu Han, SeungHwan Hong, Sean Park", True, "Yellow")
        CREDITS_RECT2 = CREDITS_TEXT.get_rect(center=(350, 300))
        SCREEN.blit(CREDITS_TEXT2, CREDITS_RECT2)
        CREDITS_TEXT3 = get_font(30).render("HeeSoo Lim, Donghyun Jung", True, "Yellow")
        CREDITS_RECT3 = CREDITS_TEXT.get_rect(center=(350, 400))
        SCREEN.blit(CREDITS_TEXT3, CREDITS_RECT3)

        CREDITS_BACK = Button(image=pygame.image.load("button.png"), pos=(640, 550), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        CREDITS_BACK.changeColor(CREDITS_MOUSE_POS)
        CREDITS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS_BACK.checkForInput(CREDITS_MOUSE_POS):
                    options()
        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("ACID RAIN", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("button.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("button.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("button.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(60), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()

