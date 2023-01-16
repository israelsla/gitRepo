
def ex1():
    name = input("What is your name: ")
    age = int(input("How old are you: "))
    year = 2022 - age + 100
    print(name + ", you will be 100 years old in the year " + str(year))
    import datetime
    current_year = datetime.datetime.now().year
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    print(f"{name}, you will be 100 years old in {current_year - age + 100}")


def ex2():
    num = int(input("give me a number "))
    check = int(input("give me a number to divide by: "))

    if num % 4 == 0:
        print(num, "is a multiple of 4")
    if num & 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")
    if num % check == 0:
        print(num, "divides evenly by", check)
    else:
        print(num, "does not divide evenly by", check)


def ex3():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for number in a:
        if number < 5:
            print(number)


def ex4():
    num = int(input("Please choose a number to divide: "))
    listRange = list(range(1, num + 1))
    divisorList = []
    for number in listRange:
        if num % number == 0:
            divisorList.append(number)
    print(divisorList)


def ex5():
    a = list(input())
    b = list(input())
    c = []
    for i in a:
        if i in b and i not in c:
            c.append([i])
    print(c)


def ex9():
    import random
    rd = random.randint(1, 9)
    guess = 0
    c = 0
    while guess != rd and guess != "exit":
        guess = int(input("enter a guess between 1 until 9 \n <<<<>>>>  "))

        if guess == "exit":
            break
        c = c + 1
        if guess > rd:
            print("Too high ")
        elif guess < rd:
            print("Too low  ")
        else:
            print("yow win the game!!!! ")
            print("Right!")
            print("You took only", c, "tries!")









def chekPalindrom(p):
    SP = str(p)
    RP = SP[::-1]
    if SP == RP:
        print("palindrome")
    else:
        print("not palindrome")


def Target():
    target = 5
    total = 1
    counter = 1
    while counter <= target:
        total = total * counter
        print(counter, ':', total)
        counter += 1


def password():
    password = 'secret'
    user_input = input('please enter your password ')
    while user_input != password:
        user_input = input("worng password, please try again.... ")

    print('correct pasword')

def number_isdogit():
    number = input("please enter your number ")
    while not number.isdigit():
        number = input("this is not a valid number, please try again...")

    print('thank you, you have enterd the number', number)

def secret_number():
    secretNumber = 100
    tries = 5
    conter = 0

    guess = int(input("please enter your guess "))
    while guess != secretNumber:
        if guess < secretNumber:
            print("Too low ")
        else:
            print("Too high ")
        conter += + 1
        if conter == tries:
            break
        guess = int(input("Tray again please.."))

    if conter < tries:
        print("congratolions, you win ")
    else:
        print("you used all of your tries, sorry...")


def Sale():
    prices = ['339', '440', '449', '560', '234', '120', '345', '678', '243', '137']
    sales = prices
    target = 500
    for day in sales:
        if day >= target:
            print(f'{day} - Target reached!')
        else:
            print(f'{day} - Target missed!... ')


def Multiplication_Table():
    for row in range(1, 11):
        for column in range(1, 11):
            print(f'{row * column:3d}', end='|')
        print()


def ex16():
    import random
    nums = []
    for i in range(20):
        nums.append(random.randint(1, 25))
        for i in range(nums.count(1)):
            nums.remove(1)
    print(nums)

    # nums = list(input("enter your list <><>"))
    points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
    points.insert(3,8)
    print(points)


def ex18():
    import random
    numberComputer = random.randint(0, 9999)
    numberMan = int(input("please enter your number <><> "))


if __name__ == '__main__':
    ex9()


