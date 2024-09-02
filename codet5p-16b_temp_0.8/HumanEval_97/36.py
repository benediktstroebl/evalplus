
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

    
    result = 0
    
    if (a == 0 or b == 0):
        return 0
    else:
        if (a < 0 and b < 0):
            a = -1*a
            b = -1*b
            result = multiply(a, b)
        else:
            a = abs(a)
            b = abs(b)
            
            while (a!= 0):
                result = result + (a%10)*(b%10)
                a = a//10
                b = b//10
    
    return result

