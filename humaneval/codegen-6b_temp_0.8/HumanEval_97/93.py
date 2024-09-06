
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
    
    # no need to worry about letter/number symbols
    # (ie. a - 1, z - 26, etc.)
    # (ie. 1 - 19, 2 - 18, etc.)
    # (ie. a - 19, b - 18, etc.)
    # (ie. 0 - 1, 1 - 2, 2 - 3, etc.)
    # (ie. 1 - 1, 2 - 1, 3 - 1, etc.)
    # so easy to just do
    
    a = abs(a)
    b = abs(b)
    
    result = 0
    
    while a > 0 and b > 0:
        if a % 10 > b % 10:
            result += b
        else:
            result += a
        a //= 10
        b //= 10
    
    if a > 0:
        result += a
    if b > 0:
        result += b
    
    return result

