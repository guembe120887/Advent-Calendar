textInput = open("./Day 2/input.txt", "r")

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

_DEBUG = False

# textInput = open("Day 2/exampleInput1.txt", "r")
# _DEBUG = True
# exampleResponse = 8

# textInput = open("Day 1/exampleInput2.txt", "r")
# exampleResponse = 281

def setPossible(cubeSet):
    cubes = cubeSet.split(",")
    for cube in cubes:
        cube = cube.split()
        color = cube[1]
        value = int(cube[0])

        if color == "red" and value > MAX_RED:
            return False
        elif color == "green" and value > MAX_GREEN:
            return False
        elif color == "blue" and value > MAX_BLUE:
            return False
    return True

def gamePossible(infoGame):
    cubeSets = infoGame.split(";")
    for cubeSet in cubeSets:
        if not setPossible(cubeSet):
            return False
    return True

def getInformation(line):
    gameId = line.split()[1][:-1]
    info = line.split(":")[1]

    return int(gameId), info

def sumIdsPossible(textInput):
    sumIds = 0
    for line in textInput:
        gameId, infoGame = getInformation(line)
        sumIds += gameId if gamePossible(infoGame) else 0

    return sumIds

response = sumIdsPossible(textInput)

if _DEBUG:
    if response == exampleResponse:
        print("OK")
    else:
        print("Error")
        print("Expected: ", exampleResponse)
        print("Received: ", response)
else:
    print(response)
