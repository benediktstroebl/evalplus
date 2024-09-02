
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
    
    # Convert the integer inputs to strings, so we can access the last characters
    a = str(a)
    b = str(b)
    # Convert the last characters of a and b to integers
    a_unit = int(a[-1])
    b_unit = int(b[-1])
    # Multiply the unit digits
    unit = a_unit * b_unit
    
    return unit

