
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
    
    sign, a = a/abs(a), abs(a)
    sign, b = b/abs(b), abs(b)
    
    result = []
    i = 0
    while a > 0:
        while i < b:
            result.append(a%10)
            i += 1
            a //= 10
        if i == b:
            result.append(a)
            i = 0
        elif i < b:
            result += ([0]*i)
            break
        
    result = sign*(reduce(lambda x, y: x*y, result))
    return result

