
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
    a = int(a)
    b = int(b)
    while a >= 1000000000:
        a = a // 1000000000
        b = b // 1000000000
    while a < 1000000000:
        a = a * 1000000000
        b = b * 1000000000
    while b >= 1000000000:
        b = b // 1000000000
        a = a // 1000000000
    while b < 1000000000:
        b = b * 1000000000
        a = a * 1000000000
    while a >= 10000:
        a = a // 1000
        b = b // 1000
    while b >= 1000:
        b = b // 100
        a = a // 10
    while a > 0:
        if a % 10 == b % 10:
            a = a // 10
        else:
            product = product * 10 + (a % 10) * (b % 10)
            a = a // 10
            b = b // 10
    return product