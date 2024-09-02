
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
    sign = 1 if a > 0 else -1
    a *= sign
    b *= sign
    
    digits = [0]*9
    
    for i in range(9):
        if a == 0: break
        digits[i] += 1 if a % 10 == 1 else 0
        a //= 10
    
    sign = -1 if b < 0 else 1
    b *= sign
    
    for i in range(9):
        if b == 0: break
        digits[i] += 1 if b % 10 == 1 else 0
        b //= 10
        
    res = 0
    for i in range(9):
        res += digits[i] * (10**i)
    
    if sign == -1: res = -res
    
    return res
