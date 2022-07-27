



def math_Add(numberOne, numberTwo):
    print(numberOne + numberTwo)


def math_Sub(numberOne, numberTwo):
    print (numberOne - numberTwo)


def math_Divide(numberOne, numberTwo):
    print (numberOne / numberTwo)

def math_X(numberOne, numberTwo):
    print (numberOne * numberTwo)


user_Question = input("What operation would you like to use? ")


if user_Question == "+":

    number_One = input("Number one > ")
    number_Two = input("Number two > ")

    math_Add(int(number_One), int(number_Two))

elif user_Question == "-":
    number_One = input("Number one > ")
    number_Two = input("Number two > ")

    math_Sub(int(number_One), int(number_Two))

elif user_Question == "/":
    number_One = input("Number one > ")
    number_Two = input("Number two > ")

    math_Divide(int(number_One), int(number_Two))

elif user_Question == "*":
    number_One = input("Number one > ")
    number_Two = input("Number two > ")

    math_X(int(number_One), int(number_Two))

else:
    exit(0)


