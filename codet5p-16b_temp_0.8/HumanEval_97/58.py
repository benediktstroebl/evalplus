
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
        return -1
    if a == 0 or b == 0:
        return 0
    
    result = 0
    
    while a > 0:
        temp = a % 10
        a = a // 10
        
        while b > 0:
            temp_b = b % 10
            b = b // 10
            
            result = result + temp * temp_b
            
            if result > 9:
                result = result % 10
                
    return result
    
