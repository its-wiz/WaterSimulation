import pygame  
import random

background_colour = (234, 212, 252)
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('Fluid!')
running = True
SIZE = 5

def RoundPos(x, base=SIZE):
    return base * round(x/base)

def isObjectAtPos(posX, posY):
    for i in range(SIZE):
        for p in range(SIZE):
            if screen.get_at((posX + i,posY + p))[:3] == (128,197,222):
                return True
            if screen.get_at((posX + i,posY + p))[:3] == (136,140,141):
                return True
    return False

class Water():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def update(self):
        if self.y < 880 and self.x < 1180 and self.x >= 20: 
            if isObjectAtPos(self.x, self.y + SIZE) == False:
                self.y = self.y + SIZE
            if isObjectAtPos(self.x, (self.y + SIZE) - 1) == False:
                self.y = self.y + SIZE
            elif isObjectAtPos(self.x-SIZE, self.y) == False and isObjectAtPos(self.x+SIZE, self.y) == False:
                rand = random.randint(0,1)
                if rand == 0: self.x = self.x - SIZE
                if rand == 1: self.x = self.x + SIZE
            elif isObjectAtPos(self.x-SIZE, self.y) == False:
                self.x = self.x - SIZE
            elif isObjectAtPos(self.x+SIZE, self.y) == False:
                self.x = self.x + SIZE 
        screen.fill((128,197,222), ((self.x, self.y), (SIZE, SIZE)))

class Stone():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def update(self):
        if self.y < 880 and self.x < 1180 and self.x >= 20: 
            screen.fill((136,140,141), ((self.x, self.y), (SIZE, SIZE)))

WaterObjects = []
StoneObjects = []
amount = 1

while running:    
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False
        try:
            if pygame.mouse.get_pressed()[0]:
                for _ in range(amount): WaterObjects.append(Water(RoundPos(event.pos[0]), RoundPos(event.pos[1])))
            if pygame.mouse.get_pressed()[2]:
                for _ in range(amount): StoneObjects.append(Stone(RoundPos(event.pos[0]), RoundPos(event.pos[1])))
        except: 
            pass

    screen.fill(background_colour)

    for stone in StoneObjects: 
        stone.update()

    for water in WaterObjects: 
        water.update()
    pygame.display.update()