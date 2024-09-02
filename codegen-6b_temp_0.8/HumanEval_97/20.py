
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
    
    # multiply method requires the input to be a string not a list.
    # this is to simplify the base case handling.
    a = str(a)
    b = str(b)
    
    # int() is required to convert from strings to integers for the 
    # multiplication.
    result = int(a) * int(b)
    
    return result


    
