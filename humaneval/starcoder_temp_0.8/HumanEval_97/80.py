
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
    
    a1 = abs(a)
    b1 = abs(b)
    sum = 0
    
    while a1:
        sum += (a1 % 10) * (b1 % 10)
        a1 = a1//10
        b1 = b1//10
        
    if sum >= 0:
        return sum
    else:
        return -sum
