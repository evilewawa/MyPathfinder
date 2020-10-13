import pygame
from square import square
import time

width = 700
height = 600


class button:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = (x, y, 25, 25)
        self.color = (0,0,0)

    def press(self):
        if pygame.mouse.get_pressed()[0]:
            cord = pygame.mouse.get_pos()
            if self.x + 25 > cord[0] >= self.x:
                if self.y + 25 > cord[1] >= self.y:
                    return True
        return False

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)


screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Client")

dif = 20

grid = []
for i in range(60, width - 60, dif):
    row = []
    for j in range(60, height - 60, dif):
        sq = square(i, j)
        row.append(sq)
    grid.append(row)


def redrawWindow(win, b,butt):
    win.fill((255, 255, 255))
    for row in grid:
        for sq in row:
            sq.draw(win)
    b.draw(win)
    butt.draw(win)
    pygame.display.update()


def findSquare(cord):
    for row in grid:
        for s in row:
            if s.x == cord[0] and s.y == cord[1]:
                return s
    return "not found"


def main():
    run = True
    # clock = pygame.time.Clock()
    twoNums = 0
    start = "square(0, 0)"
    end = "square(0, 0)"
    sqaure = square(0, 0)
    importantSquares = []
    doneSquares = []
    walls = []

    b = button(500, height - 40)
    butt = button(0,0)
    butt.color = (255,0,0)

    pressed = False
    spressed = False

    path = []
    while run:
        # clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
        redrawWindow(screen, b, butt)

        if pygame.mouse.get_pressed()[0]:
            mousePos = pygame.mouse.get_pos()
            mouseX = mousePos[0]
            mouseY = mousePos[1]
            for row in grid:
                for s in row:
                    cord = [s.x, s.y]
                    if cord[1] + dif > mouseY >= cord[1]:
                        if cord[0] + dif > mouseX >= cord[0]:
                            if twoNums == 0:
                                start = s
                                s.important = 1
                                s.color = (0, 0, 255)
                                twoNums += 1
                                time.sleep(.2)
                                importantSquares.append(s)
                            elif twoNums == 1:
                                end = s
                                s.important = 2
                                s.color = (0, 255, 0)
                                twoNums += 1
                                time.sleep(.2)
                            else:
                                if not spressed:
                                    if s.important == 0:
                                        s.important = 3
                                        s.color = (0, 0, 0)
                                        if s not in walls:
                                            walls.append(s)
                                else:
                                    if s.important == 3:
                                        s.important = 0
                                        s.color = (255,0,0)
                                        walls.pop(walls.index(s))


        for row in grid:
            for s in row:
                if s in doneSquares:
                    s.color = (0, 0, 150)
                elif s.important == 1:
                    s.color = (0, 0, 255)
                    if s not in importantSquares:
                        importantSquares.append(s)
        if b.press():
            pressed = True
        if butt.press():
            spressed = not spressed
        if len(importantSquares) == 0 and type(start) == type(sqaure):
            break
        if type(start) == type(sqaure) and type(end) == type(sqaure) and pressed:
            if end.important != 1:
                #print(importantSquares)
                for sq in importantSquares:
                    cord = [sq.x, sq.y]
                    up, down, right, left = False, False, False, False
                    upSq = findSquare([cord[0] - 20, cord[1]])
                    downSq = findSquare([cord[0] + 20, cord[1]])
                    rightSq = findSquare([cord[0], cord[1] + 20])
                    leftSq = findSquare([cord[0], cord[1] - 20])

                    if type(upSq) != type(
                            "s") and upSq not in doneSquares and upSq.important != 3 \
                            and upSq not in importantSquares:
                        up = True
                        upSq.important = 1
                        upSq.count +=1
                        upSq.prevSq = sq
                    if type(downSq) != type(
                            "s") and downSq not in doneSquares and downSq.important \
                            != 3 and downSq not in importantSquares:
                        down = True
                        downSq.important = 1
                        downSq.count += 1
                        downSq.prevSq = sq
                    if type(rightSq) != type(
                            "s") and rightSq not in doneSquares and rightSq.important != 3\
                            and rightSq not in importantSquares:
                        right = True
                        rightSq.important = 1
                        rightSq.count +=1
                        rightSq.prevSq = sq

                    if type(leftSq) != type(
                            "s") and leftSq not in doneSquares and leftSq.important != 3 \
                            and leftSq not in importantSquares:
                        left = True
                        leftSq.important = 1
                        leftSq.count+=1
                        leftSq.prevSq = sq

                    if not up and not down and not right and not left:
                        importantSquares.pop(importantSquares.index(sq))
                        doneSquares.append(sq)

            else:
                prevSqr = end.prevSq
                while type(prevSqr) == type(sqaure):
                    path.append(prevSqr)
                    prevSqr = prevSqr.prevSq
                for sq in path:
                    sq.color = (0,255,0)




main()
pygame.quit()
