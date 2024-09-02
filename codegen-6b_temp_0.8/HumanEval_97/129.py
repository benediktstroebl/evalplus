
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
    if len(str(a)) > len(str(b)):
        b, a = a, b
    a = abs(a)
    b = abs(b)

    res = 0
    for i in range(1, len(str(a))+1):
        if (len(str(a))-i) < 0: break
        digit = int(str(a)[-i])
        res += int(str(b)[-i]) * digit
    if a < 0:
        res *= -1
    return res
