
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
    return int(unitsdigit(a)[0] * unitsdigit(b)[0] + unitsdigit(a)[1] * unitsdigit(b)[1] + unitsdigit(a)[2] * unitsdigit(b)[2])
