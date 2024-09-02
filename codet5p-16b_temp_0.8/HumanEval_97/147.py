
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

    assert isinstance(a, int), 'a must be of type int'
    assert isinstance(b, int), 'b must be of type int'
    if (a >= 0 and b >= 0):
        return int(str(a)[0]) * int(str(b)[0])
    elif (a < 0 and b >= 0):
        return -1 * int(str(abs(a))[0]) * int(str(b)[0])
    elif (a >= 0 and b < 0):
        return -1 * int(str(a)[0]) * int(str(abs(b))[0])
    else:
        return int(str(abs(a))[0]) * int(str(abs(b))[0])
    pass
