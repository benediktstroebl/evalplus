
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
    n = str(int(a) + int(b))
    d = str(int(n[0]))
    while len(d) < 3:
        d = "0" + d
    while len(d) >= 3:
        n = n[:-1]
        d = d[:-1]
    return int(d) * int(n[-1])
