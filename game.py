import time
import pygame
import os
import random

pygame.init()

SCREENWIDTH = 800
SCREENHEIGHT = 600

WINDOW = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Stone Paper Scissor Game")

BASE_DIR = os.getcwd()
IMAGE = {
    "PAPER": pygame.image.load(os.path.join(BASE_DIR, 'Images\\paper.png')),
    "STONE": pygame.image.load(os.path.join(BASE_DIR, 'Images\\stone.png')),
    "SCISSOR": pygame.image.load(os.path.join(BASE_DIR, 'Images\\scissor.png')),
    "WIN": pygame.image.load(os.path.join(BASE_DIR, 'Images\\you_win.jpg')),
    "LOSE": pygame.image.load(os.path.join(BASE_DIR, 'Images\\you_lose.jpg')),
}
LABEL = {
    "PAPER": pygame.image.load(os.path.join(BASE_DIR, 'Images\\paper_label.png')),
    "STONE": pygame.image.load(os.path.join(BASE_DIR, 'Images\\stone_label.png')),
    "SCISSOR": pygame.image.load(os.path.join(BASE_DIR, 'Images\\scissor_label.png')),
    "PLAY AGAIN": pygame.image.load(os.path.join(BASE_DIR, 'Images\\play_again_label.png')),
    "COMPUTER": pygame.image.load(os.path.join(BASE_DIR, 'Images\\computer_label.png')),
    "PLAYER": pygame.image.load(os.path.join(BASE_DIR, 'Images\\player_label.png')),
}

IMAGE["PAPER"] = pygame.transform.scale(IMAGE["PAPER"], (250, 250)).convert_alpha()
IMAGE["STONE"] = pygame.transform.scale(IMAGE["STONE"], (250, 250)).convert_alpha()
IMAGE["SCISSOR"] = pygame.transform.scale(IMAGE["SCISSOR"], (250, 250)).convert_alpha()
IMAGE["WIN"] = pygame.transform.scale(IMAGE["WIN"], (250, 250)).convert_alpha()
IMAGE["LOSE"] = pygame.transform.scale(IMAGE["LOSE"], (250, 250)).convert_alpha()

EXIT_GAME = False
FPS_CLOCK = pygame.time.Clock()
FPS = 70

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (135, 206, 235)
GOLD = (255, 215, 0)
GREEN = (0, 255, 0)


def compare(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    if player_choice == "STONE" and computer_choice == "PAPER":
        return "lose"
    if player_choice == "STONE" and computer_choice == "SCISSOR":
        return "win"
    if player_choice == "PAPER" and computer_choice == "STONE":
        return "win"
    if player_choice == "PAPER" and computer_choice == "SCISSOR":
        return "lose"
    if player_choice == "SCISSOR" and computer_choice == "PAPER":
        return "win"
    if player_choice == "SCISSOR" and computer_choice == "STONE":
        return "lose"


class Button:
    def __init__(self, text, color, x, y, width, height):
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(WINDOW, self.color, [self.x, self.y, self.width, self.height])
        WINDOW.blit(self.text, (self.x, self.y))

    def isHover(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


def gameLoop():
    global EXIT_GAME
    player_choice = None
    computer_choice = None
    stone_button = Button(LABEL["STONE"], YELLOW, 300, 400, 150, 38)
    paper_button = Button(LABEL["PAPER"], YELLOW, 300, 450, 150, 38)
    scissor_button = Button(LABEL["SCISSOR"], YELLOW, 300, 500, 150, 38)

    while not EXIT_GAME:
        for event in pygame.event.get():
            position = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                EXIT_GAME = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if stone_button.isHover(position):
                    player_choice = "STONE"
                elif paper_button.isHover(position):
                    player_choice = "PAPER"
                elif scissor_button.isHover(position):
                    player_choice = "SCISSOR"
                computer_choice = random.choice(["STONE", "PAPER", "SCISSOR"])

        WINDOW.fill(GREEN)
        WINDOW.blit(LABEL["PLAYER"], (20, 20))
        WINDOW.blit(LABEL["COMPUTER"], (630, 20))
        stone_button.draw()
        paper_button.draw()
        scissor_button.draw()

        if player_choice is not None and computer_choice is not None:
            WINDOW.blit(IMAGE[computer_choice], (500, 100))
            WINDOW.blit(IMAGE[player_choice], (30, 100))
            pygame.display.update()
            time.sleep(2)
            return compare(player_choice, computer_choice)

        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def showResult(r):
    global EXIT_GAME
    play_again_button = Button(LABEL["PLAY AGAIN"], YELLOW, 350, 500, 150, 38)
    while not EXIT_GAME:
        for event in pygame.event.get():
            position = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                EXIT_GAME = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.isHover(position):
                    return

        WINDOW.fill(GREEN)
        if r == "win":
            WINDOW.blit(IMAGE["WIN"], (300, 100))
        elif r == "lose":
            WINDOW.blit(IMAGE["LOSE"], (300, 100))

        play_again_button.draw()
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


if __name__ == '__main__':
    while not EXIT_GAME:
        result = gameLoop()
        showResult(result)
