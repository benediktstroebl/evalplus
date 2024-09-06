
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
    a, b = map(int, (a, b))
    if a == 0:
        return b
    elif b == 0:
        return 0
    else:
        return sum(int(d) * 10 ** (len(str(a)) - len(str(b))) for d in str(a) for b in str(b))
