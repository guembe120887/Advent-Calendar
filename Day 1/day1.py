textInput = open("./Day 1/input.txt", "r")

# textInput = open("Day 1/exampleInput1.txt", "r")
# exampleResponse = 142

# textInput = open("Day 1/exampleInput2.txt", "r")
# exampleResponse = 281


numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def searchNumber(line, number):
    line = line.replace(number, numbers[number])
    for letter in line:
        if letter.isdigit():
            return letter    

def searchFirst(line):
    aux = ""
    for letter in line:
        if letter.isdigit():
            return letter
        
        aux += letter
        for number in numbers.keys():
            if number in aux:
                return searchNumber(aux, number)


def searchLast(line):
    aux = ""
    for letter in line[::-1]:
        if letter.isdigit():
            return letter
        
        aux = letter + aux
        for number in numbers.keys():
            if number in aux:
                return searchNumber(aux, number)

def getCalibration(line):
    
    firstNumber = searchFirst(line)
    lastNumber = searchLast(line)

    return int(firstNumber + lastNumber)


def calibrationSum(textInput):
    sum = 0

    for line in textInput:
        sum += getCalibration(line)
    return sum


response = calibrationSum(textInput)
print(response)