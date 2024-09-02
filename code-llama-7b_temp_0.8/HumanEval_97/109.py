
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
    #convert to string
    a = str(a)
    b = str(b)
    
    #take the last char of both strings
    a = a[-1]
    b = b[-1]
    
    #return the product of the last digit in the strings
    return int(a) * int(b)
