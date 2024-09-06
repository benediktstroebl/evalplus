
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
    if (a < 0 and b < 0) or (a > 0 and b > 0) :
        sign = -1
    else:
        sign = 1
    a = abs(a)
    b = abs(b)
    res = 0
    while a != 0 or b != 0:
        b, mod = divmod(b, 10)
        res += (a % 10) * mod
        a = a // 10
    return sign * res
