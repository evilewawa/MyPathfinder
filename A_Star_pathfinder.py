import math
# this is just the same pathfinder but instead it is more centralized
# by assigning values to the squares
# did some research and found an example and
# what i figured the mentality was that
# as long as the next square in closing the distance
# you  should move to it

# to start create grid
start = 1
end = 2
border = 3
paths = []
def main():
    pathsFinder()


def getDistance(x, y):
    a = (y[1] - x[1])**2
    b= (y[0]-x[0])**2
    return math.sqrt(a+b)



def printGrid(grid):
    for row in grid:
        for col in row:
            if len(str(col)) == 1:
                print(" " + str(col), end=", ")
            else:
                print(col, end= ", ")
        print("")


def findInGrid(grid, num):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == num:
                return [i, j]
    return None

def shouldUp(distances, grid, sq):
    if sq[0] > 0:
        if grid[sq[0]-1][sq[1]] != border:
            if distances[sq[0]][sq[1]] > distances[sq[0]-1][sq[1]]:
                return True


def shouldDown(distances, grid, sq):
    if sq[0] < len(grid)-1:
        if grid[sq[0]+1][sq[1]] != border:
            if distances[sq[0]][sq[1]] > distances[sq[0]+1][sq[1]]:
                return True


def shouldLeft(distances, grid, sq):
    if sq[1] > 0:
        if grid[sq[0]][sq[1]-1] != border:
            if distances[sq[0]][sq[1]] > distances[sq[0]][sq[1]-1]:
                return True


def shouldRight(distances, grid, sq):
    if sq[1] < len(grid)-1:
        if grid[sq[0]][sq[1] + 1] != border:
            if distances[sq[0]][sq[1]] > distances[sq[0]][sq[1]+1]:
                return True


def pathsFinder():
    grid = [[0 for j in range(100)] for i in range(100)]
    grid[len(grid)-1][len(grid)-1] = start
    grid[0][0] = end
    goal = findInGrid(grid, end)
    s = findInGrid(grid, start)
    distances = [[getDistance([i, j], goal) for j in range(len(grid[i]))]for i in range(len(grid))]
    path = []
    pathfinder(grid, distances, s, path)
    for i in range(len(path)):
        loc = path[i]
        grid[loc[0]][loc[1]] = i+2
    printGrid(grid)


def pathfinder(grid, distances, curSq, path):
    print("bluk")
    if getDistance(curSq, findInGrid(grid, end)) == 0:
        return True
    #curSq is not end so now you need to find the squares around
    if shouldUp(distances, grid, curSq):
        path.append([curSq[0]-1, curSq[1]])
        if pathfinder(grid, distances, [curSq[0]-1, curSq[1]], path):
            return path
        path.pop()
    if shouldDown(distances, grid, curSq):
        path.append([curSq[0]+1, curSq[1]])
        if pathfinder(grid, distances, [curSq[0]+1, curSq[1]], path):
            return path
        path.pop()
    if shouldLeft(distances, grid, curSq):
        path.append([curSq[0], curSq[1]-1])
        if pathfinder(grid, distances, [curSq[0], curSq[1]-1], path):
            return path
        path.pop()
    if shouldRight(distances, grid, curSq):
        path.append([curSq[0], curSq[1]+1])
        if pathfinder(grid, distances, [curSq[0], curSq[1]+1], path):
            return path
        path.pop()
    return False

main()