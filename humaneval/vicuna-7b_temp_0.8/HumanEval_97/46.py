
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
    a, b = map(int, str(a)[2:], str(b)[2:])
    if a == 0:
        return 0
    if b == 0:
        return 0
    return int(str(a)[2] * str(b)[2]) + int(str(a)[1] * str(b)[1]) + \
        int(str(a)[0] * str(b)[0]) + int(str(a)[-1] * str(b)[-1])