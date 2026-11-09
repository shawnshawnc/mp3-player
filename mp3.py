

import pygame
pygame.init()

# Creating window
gameWindow = pygame.display.set_mode((800, 300))
pygame.display.set_caption("Event Handling")


exit_game = False
game_over = False

screen = pygame.display.set_mode((800, 600))

def printimage(image):
    img = pygame.image.load(image)
    img_small = pygame.transform.scale(img, (100, 100))
    img_large = pygame.transform.scale(img, (200, 200)) 
    running = True
    while running:
        # fill background
        screen.fill((255, 255, 255))

        # display images at different positions
           
        screen.blit(img_large, (300, 200))    

        # update display
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
# Creating a game loop


while not exit_game:
    for event in pygame.event.get():  # For Loop
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key")
            elif event.key == pygame.K_LEFT:
                printimage("ambience.jpg")

pygame.quit()
quit()