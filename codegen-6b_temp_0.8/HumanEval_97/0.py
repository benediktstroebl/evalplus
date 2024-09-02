
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
    if a == 0 or b == 0:
        return 0
    
    if a < 0 or b < 0:
        a = -a
        b = -b
    
    temp_res = 0
    while b > 0:
        temp = b % 10
        temp_res += temp * temp_res
        b = b // 10
    
    if a > 0:
        return temp_res + a
    else:
        return temp_res + a * -1
    
