import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

black = (0, 0, 0)
white = (255, 255, 255)
red = (190, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

pygame.display.set_caption("dont get hit by the hay")
clock = pygame.time.Clock()
pause = False

def smallText(x, y, text):
    smallText = pygame.font.Font("/Library/Fonts/Amatic-Bold.ttf", 35)
    small_TextSurf, small_TextRect = text_objects(text, smallText)
    small_TextRect.center = (x, y)
    gameDisplay.blit(small_TextSurf, small_TextRect)

def medText(x, y, text):
    medText = pygame.font.Font("/Library/Fonts/Amatic-Bold.ttf", 50)
    med_TextSurf, med_TextRect = text_objects(text, medText)
    med_TextRect.center = (x, y)
    gameDisplay.blit(med_TextSurf, med_TextRect)

def things_dodged(count):
    font = pygame.font.Font("/Library/Fonts/Amatic-Bold.ttf", 100)
    text = font.render(str(count), True, black)
    gameDisplay.blit(text, (display_width/2, 0))

def instructions():
    font = pygame.font.Font("/Library/Fonts/Amatic-Bold.ttf", 35)
    text = font.render("press the LEFT and RIGHT arrow keys!", True, black)
    space = font.render("press SPACEBAR to pause!", True, black)
    gameDisplay.blit(text, (5, 40))
    gameDisplay.blit(space, (5, 80))

def hay(thingx, thingy, thingw, thingh):
    hayImg = pygame.image.load("hay.png")
    gameDisplay.blit(hayImg, [thingx, thingy, thingw, thingh])

def pig(x, y):
    pigImg = pygame.image.load("pig.png")
    gameDisplay.blit(pigImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("/Library/Fonts/Amatic-Bold.ttf", 125)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    escape()
    message_display("you got hit by the hay!")

def hit_wall():
    escape()
    message_display("you ran into the wall!")

def escape():
    escapeText = "press ESC to go back!"
    smallText(90, 20, escapeText)

def game_credits():
    credits = True
    while credits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_intro()

        gameDisplay.fill(white)
        escape()
        credits_smallText1 = "thank you for playing my first python game."
        credits_smallText2 = "special thanks to sentdex for teaching me how to use pygame:"
        credits_smallText3 = " https://www.youtube.com/user/sentdex/"
        medText((display_width / 2), (100), "HELLO WORLD!")
        medText((display_width / 2), (150), credits_smallText1)
        medText((display_width / 2), (225), credits_smallText2)
        medText((display_width / 2), (275), credits_smallText3)

        hayImg = pygame.image.load("hay.png")
        pigImg = pygame.image.load("pig.png")
        gameDisplay.blit(hayImg, (200, 480))
        pigImg_hoFlip = pygame.transform.flip(pigImg, True, False)
        gameDisplay.blit(pigImg_hoFlip, (220, 375))
        pygame.display.update()
        clock.tick(15)

def unpaused():
    global pause
    pause = False

def paused():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False
                    unpaused()
                if event.key == pygame.K_ESCAPE:
                    game_intro()

        largeText = pygame.font.Font("/Library/Fonts/Amatic-Bold.ttf", 125)
        TextSurf, TextRect = text_objects("paused", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font("/Library/Fonts/Amatic-Bold.ttf", 125)
        TextSurf, TextRect = text_objects("dont get hit by the hay", largeText)
        TextRect.center = ((display_width / 2), (display_height / 10))
        gameDisplay.blit(TextSurf, TextRect)

        secondary_largeText = pygame.font.Font("/Library/Fonts/Amatic-Bold.ttf", 40)
        secondary_TextSurf, secondary_TextRect = text_objects("by: elijah delos reyes", secondary_largeText)
        secondary_TextRect.center = ((display_width / 1.5), (display_height / 4))
        gameDisplay.blit(secondary_TextSurf, secondary_TextRect)

        hayImg = pygame.image.load("hay.png")
        hayImg_320 = pygame.transform.rotate(hayImg, 320)
        hayImg_40 = pygame.transform.rotate(hayImg, 40)
        pigImg = pygame.image.load("pig.png")
        gameDisplay.blit(hayImg, (0, 480))
        gameDisplay.blit(hayImg, (235, 480))
        gameDisplay.blit(hayImg, (0, 370))
        gameDisplay.blit(hayImg_320, (170, 260))
        gameDisplay.blit(hayImg_40, (20, 150))
        gameDisplay.blit(pigImg, (530, 480))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 410 + 345 > mouse[0] > 410 and 205 + 50 > mouse[1] > 205:
            pygame.draw.polygon(gameDisplay, black, ((440, 255), (420, 250), (415, 245), (415, 215), (420, 210),
                                                     (440, 205), (730, 205), (750, 210), (755, 215), (755, 245),
                                                     (750, 250), (730, 255)))
            pygame.draw.polygon(gameDisplay, white, ((441, 254), (421, 249), (416, 244), (416, 216), (421, 211),
                                                     (441, 206), (731, 206), (749, 211), (754, 215), (754, 244),
                                                     (749, 249), (729, 254)))
            medText(575, 225, "PLAY!")
            if click[0] == 1:
                game_loop()
        else:
            pygame.draw.polygon(gameDisplay, black, ((440, 255), (420, 250), (415, 245), (415, 215), (420, 210),
                                                     (440, 205), (730, 205), (750, 210), (755, 215), (755, 245),
                                                     (750, 250), (730, 255)))
            pygame.draw.polygon(gameDisplay, white, ((451, 254), (431, 249), (426, 244), (426, 216), (431, 211),
                                                     (451, 206), (721, 206), (739, 211), (744, 215), (744, 244),
                                                     (739, 249), (719, 254)))
            smallText(575, 225, "play")

        if 410 + 345 > mouse[0] > 410 and 280 + 50 > mouse[1] > 280:
            pygame.draw.polygon(gameDisplay, black, ((440, 330), (420, 325), (415, 320), (415, 290), (420, 285),
                                                     (440, 280), (730, 280), (750, 285), (755, 290), (755, 320),
                                                     (750, 325), (730, 330)))
            pygame.draw.polygon(gameDisplay, white, ((441, 329), (421, 324), (416, 319), (416, 291), (421, 286),
                                                     (441, 281), (731, 281), (749, 286), (754, 290), (754, 319),
                                                     (749, 324), (729, 329)))
            medText(575, 300, "CREDITS")
            if click[0] == 1:
                game_credits()
        else:
            pygame.draw.polygon(gameDisplay, black, ((440, 330), (420, 325), (415, 320), (415, 290), (420, 285),
                                                     (440, 280), (730, 280), (750, 285), (755, 290), (755, 320),
                                                     (750, 325), (730, 330)))
            pygame.draw.polygon(gameDisplay, white, ((451, 329), (431, 324), (426, 319), (426, 291), (431, 286),
                                                     (451, 281), (721, 281), (739, 286), (744, 290), (744, 319),
                                                     (739, 324), (719, 329)))
            smallText(575, 300, "credits")

        if 410 + 345 > mouse[0] > 410 and 355 + 50 > mouse[1] > 355:
            pygame.draw.polygon(gameDisplay, black, ((440, 405), (420, 400), (415, 395), (415, 365), (420, 360),
                                                     (440, 355), (730, 355), (750, 360), (755, 365), (755, 395),
                                                     (750, 400), (730, 405)))
            pygame.draw.polygon(gameDisplay, white, ((441, 404), (421, 399), (416, 394), (416, 366), (421, 361),
                                                     (441, 356), (731, 356), (749, 361), (754, 365), (754, 394),
                                                     (749, 399), (729, 404)))
            medText(575, 375, "quit :(")
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.polygon(gameDisplay, black, ((440, 405), (420, 400), (415, 395), (415, 365), (420, 360),
                                                     (440, 355), (730, 355), (750, 360), (755, 365), (755, 395),
                                                     (750, 400), (730, 405)))
            pygame.draw.polygon(gameDisplay, white, ((451, 404), (431, 399), (426, 394), (426, 366), (431, 361),
                                                     (451, 356), (721, 356), (739, 361), (744, 365), (744, 394),
                                                     (739, 399), (719, 404)))
            smallText(575, 375, "quit")
        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    # Set pig
    pig_width = 160
    x = 530
    y = (display_height * 0.8)
    x_change = 0
    thing_startx = random.randrange(50, display_width - 50)
    thing_starty = -300
    thing_speed = 7
    thing_width = 190
    thing_height = 80
    dodged = 0

    # Set game-loop
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -20
                if event.key == pygame.K_RIGHT:
                    x_change = 20
                if event.key == pygame.K_SPACE:
                    pause = True
                    paused()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_intro()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x = x + x_change

        # Draw things
        gameDisplay.fill(white)
        hay(thing_startx, thing_starty, thing_width, thing_height)
        thing_starty = thing_starty + thing_speed
        pig(x, y)
        instructions()
        things_dodged(dodged)

        # Set boundaries
        if x > display_width - pig_width or x < 0:
            hit_wall()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randint(0, display_width)
            dodged = dodged + 1
            thing_speed = thing_speed + 1
        if y < thing_starty + thing_height:
            if thing_startx < x + pig_width and thing_startx + thing_width > x:
                crash()

        escape()
        # Update anything eg. background
        pygame.display.update()
        # Set fps
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
