
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
    from math import floor, log10
    if not b:
        return 0
    a, b = abs(a), abs(b)
    res = 0
    for i in range(1, ceiling(log10(a) + 1)):
        res += (a % b + 10) * (a // b)
        a %= b
    return floor(res)
