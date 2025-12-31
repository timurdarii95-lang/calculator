for i in range(3):

    nr1 = int(input('Enter your first number: '))
    nr2 = int(input('Enter your second number: '))
    operation = input('Choose a operation: +, -, *, /: ')
    if operation == '+':
        result = nr1 + nr2
    elif operation == '-':
        result = nr1 - nr2
    elif operation == '*':
        result = nr1 * nr2
    elif operation == '/':
        if nr2 == 0:
            result = 'ERROR'
        else:
            result = nr1 / nr2
    else:
        result = 'Invalid operation'
    print('Your result is: ', result)