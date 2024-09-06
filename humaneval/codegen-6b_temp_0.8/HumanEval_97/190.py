
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
    s1 = str(a)
    s2 = str(b)
    r = list(map(int, s1))
    c = list(map(int, s2))
    res = [a*b for a,b in zip(r,c)]
    print(''.join(map(str,res)))


multiply(148, 412)
multiply(19, 28)
multiply(2020, 1851)
multiply(14,-15)
