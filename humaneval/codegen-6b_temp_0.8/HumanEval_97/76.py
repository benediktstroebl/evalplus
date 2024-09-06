
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
    multiply = 1
    if a == -1 or b == -1:
        return None
    a = abs(a)
    b = abs(b)
    while a > 0:
        remainder = b % 10
        b = b / 10
        multiply = multiply * remainder
        a = a - 1
    if multiply < 0:
        return -multiply
    return multiply

