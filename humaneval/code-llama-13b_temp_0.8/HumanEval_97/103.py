
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
    x = str(a)[::-1]
    y = str(b)[::-1]
    if a*b<0:
        return 0
    elif len(x)==1 or len(y)==1:
        return int(x)*int(y)
    else:
        return int(x[0])*int(y[0])
