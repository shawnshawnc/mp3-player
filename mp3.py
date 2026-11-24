import pygame
import random
import sys
pygame.init()

i_dont_want_to_see_my_disgusting_variables = True
if i_dont_want_to_see_my_disgusting_variables == True:
    width = 1000
    height = 750
    screen = pygame.display.set_mode((width, height))
    white = 255, 255, 255
    gray = 170, 170, 170
    darkgray = 100, 100, 100
    pygame.display.flip()
    con = True
    playlist = ["ambient", "nature", "rain"]
    image_size = (250, 250)
    font = pygame.font.SysFont("Times New Roman", 30)
    raintext = font.render("Rain Music", True, (0,0,0)) 
    naturetext = font.render("Nature Music", True, (0,0,0)) 
    ambienttext = font.render("Ambient Music", True, (0,0,0)) 
    green = (194, 218, 184)
    currentlyplaying = ""
    stop = False
    screen = pygame.display.set_mode((750,500))
    screen.fill(green)


while stop == False:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            stop = True
        pygame.display.flip()

        #skip
        skipicon = pygame.image.load("skip.png")
        skipicon = pygame.transform.scale(skipicon, (150, 100))
        screen.blit(skipicon , (100, 400))
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 100 <= mouse[0] <= 250 and 400 <= mouse[1] <= 450:
                tempvar = currentlyplaying
                playlist.remove(currentlyplaying)
                currentlyplaying = random.choice(playlist)
                playlist.append(tempvar)


        #ambient button
        screen.blit(ambienttext , (515, 300))
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 490 <= mouse[0] <= 700 and 295 <= mouse[1] <= 330 or currentlyplaying == "ambient":
                #playing music
                ambient = pygame.image.load("ambience.jpg")
                screen = pygame.display.set_mode((750,500))
                ambient = pygame.transform.scale(ambient, image_size)
                screen.fill(green)
                pygame.mixer.music.load("ambient.mp3")
                pygame.mixer.music.play()
                screen.blit(ambient, (100, 100))
                screen.blit(raintext , (533, 200))
                screen.blit(ambienttext , (515, 300))
                screen.blit(naturetext , (525, 250))
                screen.blit(skipicon , (100, 400))
                pygame.display.flip()
                currentlyplaying = "ambient"            

        #nature button
        screen.blit(naturetext , (525, 250))
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 490 <= mouse[0] <= 700 and 250 <= mouse[1] <= 290 or currentlyplaying == "nature":
                nature = pygame.image.load("nature.webp")
                screen = pygame.display.set_mode((750,500))
                nature = pygame.transform.scale(nature, image_size)
                screen.fill(green)
                pygame.mixer.music.load("nature.mp3")
                pygame.mixer.music.play()
                screen.blit(nature, (100, 100))
                screen.blit(raintext , (533, 200))
                screen.blit(ambienttext , (515, 300))
                screen.blit(naturetext , (525, 250))
                screen.blit(skipicon , (100, 400))
                pygame.display.flip()
                currentlyplaying = "nature"

        #rain button
        screen.blit(raintext , (533, 200))
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 490 <= mouse[0] <= 700 and 200 <= mouse[1] <= 240 or currentlyplaying == "rain":
                rain = pygame.image.load("rain.jpg")
                screen = pygame.display.set_mode((750,500))
                rain = pygame.transform.scale(rain, image_size)
                screen.fill(green)
                pygame.mixer.music.load("rain.mp3")
                pygame.mixer.music.play()
                screen.blit(rain, (100, 100))
                screen.blit(raintext , (533, 200))
                screen.blit(ambienttext , (515, 300))
                screen.blit(naturetext , (525, 250))
                screen.blit(skipicon , (100, 400))
                pygame.display.flip()
                currentlyplaying = "rain"

    mouse = pygame.mouse.get_pos()
    #first number is x/width second number is y/hieght
    #counts in the middle
    pygame.display.update()

pygame.quit()
sys.exit()

