
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
    
    a = str(a)
    b = str(b)
    a_result = 0
    b_result = 0
    for i in range(len(a)):
        a_result += int(a[i])
        
    for i in range(len(b)):
        b_result += int(b[i])
        
    return a_result*b_result
