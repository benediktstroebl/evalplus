
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
    # return the product of the unit digits in a and b
    return int(str(a)[-1]) * int(str(b)[-1])

    '''
    Using For loops we can do it as 
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    while(a>9):
        a = sum(int(i) for i in str(a))
    while(b>9):
        b = sum(int(i) for i in str(b))
    return a * b
    '''
