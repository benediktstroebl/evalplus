
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
    a = str(a)
    b = str(b)
    res = 0
    if len(a) == 1:
        res += a[0] * b[0]
        return res
    if len(b) == 1:
        res += a[0] * b[0]
        return res
    res += a[-1] * b[-1]
    return res
