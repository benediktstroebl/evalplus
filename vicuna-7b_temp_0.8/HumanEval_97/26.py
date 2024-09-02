
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
    # check if the number of digits is the same
    if len(str(a)) != len(str(b)):
        return 0
    
    # convert both numbers to strings and get the unit digits
    a_unit = str(a)[2:].zfill(2)
    b_unit = str(b)[2:].zfill(2)
    
    # check if the units are the same
    if a_unit != b_unit:
        return 0
    
    # convert the entire number to a number
    a_num = int(a)
    b_num = int(b)
    
    # multiply the digits of the number
    product = a_num * b_num
    
    # convert the product back to a string and get the unit digit
    product_unit = str(product)[2:].zfill(2)
    
    return product_unit