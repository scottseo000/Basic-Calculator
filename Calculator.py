#Functions for operations
def addition():
    firstNum = float(input("What is the first number to add?: "))
    secondNum = float(input("What is the second number to add?: "))
    return firstNum + secondNum
def subtraction():
    firstNum = float(input("What is the number to be subtracted from?: "))
    secondNum = float(input("What is the number to subtract?: "))
    return firstNum - secondNum

def multiplication():
    firstNum = float(input("What is the first number to multiply?: "))
    secondNum = float(input("What is the second number to multiply?: "))
    return firstNum * secondNum

def division():
    firstNum = float(input("What is the number to be divided?: "))
    secondNum = float(input("What is the number that divides?: "))
    if secondNum == 0:
        return "undefined. Cannot divide by 0."
    else:
        return firstNum / secondNum

#Check which operation user would like to do
operationType = input("What operation would you like to do? (addition, subtraction, multiplication, division): ")
operationType = operationType.lower()

match operationType:
    case "addition":
        print("The sum is: " + str(addition()))
    case "subtraction":
        print("The result is: " + str(subtraction()))
    case "multiplication":
        print("The result is: " + str(multiplication()))
    case "division":
        print("The result is: " + str(division()))
    case _:
        print("Please choose one of: addition, subtraction, multiplication, division")

