from asyncio.windows_events import NULL
import queue


def createMaze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "X", "#"])

    return maze


def printMaze(Maze):
    for i in range(len(Maze)):
        for j in range(len(Maze)):
            print(Maze[i][j], " ", end="")
        print()


def checkMovements(Maze, r, c):
    valMovements = []
    if r-1 >= 0 and Maze[r-1][c] != "#":
        valMovements.append('U')
    if r+1 < len(Maze) and Maze[r+1][c] != "#":
        valMovements.append('D')
    if c-1 >= 0 and Maze[r][c-1] != "#":
        valMovements.append('L')
    if c+1 < len(Maze) and Maze[r][c+1] != "#":
        valMovements.append('R')

    return valMovements


Maze = createMaze()
