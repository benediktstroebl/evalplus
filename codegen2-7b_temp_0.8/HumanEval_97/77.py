
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
    s = str(a*b)
    m = len(s)
    if m > 9:
        return sum(list(map(int, s[0:m-9])))/10**9
    else:
        return sum(list(map(int, s)))/10**m
