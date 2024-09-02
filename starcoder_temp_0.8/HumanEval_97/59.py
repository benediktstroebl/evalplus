
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
    if a<0:
        a = a * -1
    if b<0:
        b = b * -1
    a_string = str(a)
    b_string = str(b)
    a_unit = int(a_string[-1])
    b_unit = int(b_string[-1])
    result = a_unit * b_unit
    return result
