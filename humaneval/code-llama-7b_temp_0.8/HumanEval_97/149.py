
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
    # First, convert the inputs to a string and then to a list of
    # integers.
    a = [int(x) for x in str(a)]
    b = [int(x) for x in str(b)]
    
    # Now, get the last digit of each integer.
    a = a[-1]
    b = b[-1]
    
    return a * b

