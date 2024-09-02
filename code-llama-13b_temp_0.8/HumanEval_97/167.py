
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
    result = 1
    if a >= 0:
        a = str(a)[::-1]
        a = int(a[0])
    else:
        a = str(a)[::-1]
        a = int(a[1])
    
    if b >= 0:
        b = str(b)[::-1]
        b = int(b[0])
    else:
        b = str(b)[::-1]
        b = int(b[1])
    result = a*b
    return result

