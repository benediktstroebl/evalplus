
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
    if a < 10 and b < 10:
        return a*b
    else:
        if a < 10:
            return a * multiply(a, int(str(b)[1]))
        elif b < 10:
            return b * multiply(int(str(a)[1]), b)
        else:
            return multiply(a, int(str(b)[1])) * multiply(int(str(a)[1]), b)
