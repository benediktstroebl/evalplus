
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

    if a < 0 or b < 0:
        return multiply(-a, -b)
    
    return sum(i*j for i,j in zip((x%10 for x in (a,b)), (y%10 for y in (a,b))))

