
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
    x = abs(a)
    y = abs(b)
    mult = 0
    while x or y:
        if x % 10:
            n = x % 10
            mult = mult * 10 + n
        x = x // 10
        if y % 10:
            n = y % 10
            mult = mult * 10 + n
        y = y // 10
    return mult if a*b < 0 else mult * -1
