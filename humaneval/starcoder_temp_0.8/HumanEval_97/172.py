
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
    if a > 0:
        a1 = a % 10
    else:
        a1 = a % -10
    if b > 0:
        b1 = b % 10
    else:
        b1 = b % -10
    return a1 * b1
