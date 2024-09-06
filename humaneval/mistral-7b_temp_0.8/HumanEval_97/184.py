
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
    unit = 0
    # Checks if the numbers are negative.
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    while a > 0 or b > 0:
        if a > 0:
            a = a % 10
            unit += a
            a = a // 10
        if b > 0:
            b = b % 10
            unit += b
            b = b // 10
    return unit



