
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
    a = abs(a)
    b = abs(b)

    if a == 0 or b == 0:
        return 0

    if a < b:
        a, b = b, a

    multiplication = 1
    while b > 0:
        if b % 10 > 0:
            multiplication *= a
        a *= 10
        b /= 10

    return multiplication

