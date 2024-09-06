
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
    num = str(a)
    den = str(b)
    
    if den[0] == '1':
        while den[1] == '1':
            den = den[:-1]
        num = num[:-1]
        return int(num) * int(den)
    else:
        return 0
