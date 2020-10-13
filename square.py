import pygame


class square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = (self.x, self.y, 15, 15)
        self.color = (255, 0, 0)
        self.important = 0
        self.prevSq = ""
        self.count = 0
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def write(self):
        importance = ""
        if self.important == 1:
            importance = "start"
        elif self.important == 2:
            importance = "end"
        else:
            importance = "not"
        return "X pos:", self.x, " Y pos:", self.y, "importance:", importance
