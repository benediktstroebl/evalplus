
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
        return 0
    if b < 0:
        return -1
    while b:
        if a % 10 == b % 10:
            a, b = b, a // 10
        if b < 10:
            b += 1
        elif b > 9:
            b -= 1
    return a