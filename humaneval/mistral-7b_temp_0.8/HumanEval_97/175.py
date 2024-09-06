
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    number1 = str(a)
    number2 = str(b)
    digit1 = number1[len(number1)-1]
    digit2 = number2[len(number2)-1]
    return int(digit1) * int(digit2)
    print(multiply(148, 412))
    print(multiply(19, 28))
    print(multiply(2020, 1851))
    print(multiply(14,-15))
