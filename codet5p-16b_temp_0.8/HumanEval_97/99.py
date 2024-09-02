
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

    if a == 0 or b == 0:
        return 0
    if a < 0 or b < 0:
        return multiply(abs(a), abs(b)) * -1
    if (a < 10 and b < 10) or (a > 99 and b > 99):
        return a*b
    if a < 10:
        a = str(a)
        a = a[-1]
        a = int(a)
    else:
        a = int(a/10)
    if b < 10:
        b = str(b)
        b = b[-1]
        b = int(b)
    else:
        b = int(b/10)
    return multiply(a, b)
