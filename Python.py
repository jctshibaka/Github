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
