# while loop is used to repeat a set of statements until a condition is true.
# It is often used to iterate over a sequence of items, such as a list.
# The while loop will execute a set of statements as long as the condition is true.
# The while loop will stop when the condition is false.
# The while loop uses an if statement to check the condition.
# A while loop prints continuously until the condition is false.

# age = 23

# while age < 25:
#     if age == 24:
#         print('Age is 24')
#         # break
#     else:
#         print('Age is not 24')
#         break

# Conditional Statements is used to execute a set of statements if a certain condition is true.
# The if statement is used to check a condition.
# The if statement will execute a set of statements if the condition is true.
# The elif statement is used to check another condition to see if it is true.
# The else statement is used to execute a set of statements if the condition is false.

# age = 25
# if age == 23:
#     print('Age is 23')
# elif age == 24:
#     print('Age is 24')
# else:
#     print('Age is not 24 or 23')

# input() is used to get input from the user.
# The input() function will return a string.

# age = input('Enter your age: ')
# # age = int(age)
# # print(age)
# # print(type(age))
# while age < 25:
#     if age == 23:
#         print('Age is 23')
#         break
#     elif age == 24:
#         print('Age is 24')
#         break
#     else:
#         print('Age is not 24 or 23')
#         break

# age = int(input('Enter your age: '))
# # print(age)
# # print(type(age))
# while age < 25:
#     if age == 23:
#         print('Age is 23')
#         break
#     elif age == 24:
#         print('Age is 24')
#         break
#     else:
#         print('Age is not 24 or 23')
#         break
# import random

# RAND_INT = random.randint(1, 11)
# cont= True
# while cont:
#     guess = int(input('Guess a number between 1 and 10: '))
#     if guess == RAND_INT:
#         print('You guessed the number!')
#         cont = False
#     elif guess < RAND_INT:
#         print('Guess higher')
#     else:
#         print('Guess lower')
# print('Done')


# A function is a block of code which only runs when it is called.
# A function can take in arguments and can return a value.
# A function is defined using the 'def' keyword.
# A function can be called using the function name followed by parenthesis.

# Funtion definition without arguments
# def helloWorld():
#     print('Hello World!')
#     print('Welcome to the world of Python!')

    

# helloWorld()


# function definition with arguments
# def helloWorld(name, age, country, zipcode):
#     if country == 'NIGERIA':
#         print('Hello ' + name + '! You are ' + str(age) + ' years old and you live in ' + country + ' with the zipcode ' + zipcode)

#     print('Hello ' + name)

# helloWorld('Seyi', 23, 'NIGERIA', '23480')
# num = 5
# num2 = 10
# # Function definition with return value
# def addNum():
#     return num + num2

# addNum()
# print(addNum())
while True:
    first_num = int(input('Enter first number: '))
    symbol = input('Enter operator: ')
    second_num = int(input('Enter second number: '))


    def add_num(num1, num2):
        return num1 + num2

    def sub_num(num1, num2):
        return num1 - num2

    def mult_num(num1, num2):
        return num1 * num2

    def div_num(num1, num2):
        return num1 / num2

    if symbol == '+':
        print(add_num(first_num, second_num))
    elif symbol == '-':
        print(sub_num(first_num, second_num))
    elif symbol == '*':
        print(mult_num(first_num, second_num))
    elif symbol == '/':
        print(div_num(first_num, second_num))
    else:
        print('Invalid operator')