textInput = open("./Day 2/input.txt", "r")

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

_DEBUG = False

# textInput = open("Day 2/exampleInput1.txt", "r")
# _DEBUG = True

powers = {
    1: 48,
    2: 12,
    3: 1560,
    4: 630,
    5: 36
}

exampleResponse = 2286


def getValues(cubeSet):
    cubes = cubeSet.split(",")
    red, blue, green = 0, 0, 0
    for cube in cubes:
        cube = cube.split()
        color = cube[1]
        value = int(cube[0])

        if color == "red":
            red = value
        elif color == "green":
            green = value
        elif color == "blue":
            blue = value
    return red, blue, green

def getPower(infoGame):
    cubeSets = infoGame.split(";")
    maxRed, maxBlue, maxGreen = 0, 0, 0
    for cubeSet in cubeSets:
        red, blue, green = getValues(cubeSet)
        maxRed = max(maxRed, red)
        maxBlue = max(maxBlue, blue)
        maxGreen = max(maxGreen, green)

    return maxRed * maxBlue * maxGreen

def getInformation(line):
    gameId = line.split()[1][:-1]
    info = line.split(":")[1]

    return int(gameId), info

def sumPowers(textInput):
    sumPowers = 0
    for line in textInput:
        gameId, infoGame = getInformation(line)
        power = getPower(infoGame)
        sumPowers += power
        
        if _DEBUG:
            if power != powers[gameId]:
                print("Error in id: ", gameId)
                print("Expected: ", powers[gameId])
                print("Received: ", power)

    return sumPowers

response = sumPowers(textInput)

if _DEBUG:
    if response == exampleResponse:
        print("OK")
    else:
        print("Error")
        print("Expected: ", exampleResponse)
        print("Received: ", response)
else:
    print(response)
