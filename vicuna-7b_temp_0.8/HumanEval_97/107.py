
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
    # First check if the inputs are valid
    if not (a >= 0 and a <= 9 and b >= 0 and b <= 9):
        return -1
    
    # check for leading zeros
    if a == 0:
        return 0
    if b == 0:
        return 0
    
    # convert a and b to strings
    a_str = str(a)
    b_str = str(b)
    
    # check if the unit digits are 1
    if a_str[-1] == '1':
        a_str = a_str[:-1]
    if b_str[-1] == '1':
        b_str = b_str[:-1]
    
    # compare the two strings
    if a_str < b_str:
        return 0
    else:
        return 1