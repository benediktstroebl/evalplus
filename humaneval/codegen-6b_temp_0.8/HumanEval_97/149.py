
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
    a, b = abs(a), abs(b)
    res = 0
    factor = 1
    while b:
        if b & 1:
            res += a * factor
        a, b = a << 1, b >> 1
        factor *= 10
    return res
