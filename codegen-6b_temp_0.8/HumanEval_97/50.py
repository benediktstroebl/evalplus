
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
    isNeg = False

    if a < 0:
        a = abs(a)
        isNeg = True
    if b < 0:
        b = abs(b)
        isNeg = True

    res = 0
    while a > 0:
        res = (res * 10) + a % 10
        a = a // 10
    if isNeg:
        res = -res

    if b > 0:
        res = (res * b)
    else:
        res = -res

    return res
