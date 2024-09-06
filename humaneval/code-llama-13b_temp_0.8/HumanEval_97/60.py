
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

    a_str = str(a)
    b_str = str(b)

    a_str_unit = a_str[-1]
    b_str_unit = b_str[-1]

    a_int = int(a_str_unit)
    b_int = int(b_str_unit)
    
    return a_int * b_int
