
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
    return int(str(a*b)[0:1])+int(str(a*b)[1:2])+int(str(a*b)[2:3])+int(str(a*b)[3:4])
