
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
    if b == 0:
        return a
    elif a == 0:
        return 0
    elif a < 0 and b < 0:
        return -(abs(a) * abs(b))
    elif a < 0 and b > 0:
        return abs(a) * (abs(b) % 10)
    elif a > 0 and b < 0:
        return abs(a) * (abs(b) % 10)
    return
