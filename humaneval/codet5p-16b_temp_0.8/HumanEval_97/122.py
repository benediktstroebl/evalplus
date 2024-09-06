
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

    
    if b < 0:
        return multiply(b, -a)
    elif a == 0:
        return 0
    else:
        if a < 0:
            a = -a
        if b < 0:
            b = -b
        result = 0
        for digit in str(a):
            result += int(digit)
        return result * b
        
    
    
