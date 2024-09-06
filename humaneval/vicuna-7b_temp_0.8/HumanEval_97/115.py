
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
    # swap the digits
    a = swap(a)
    b = swap(b)
    # get the digit strings
    d = str(a)
    e = str(b)
    # get the unit digits
    c = get_unit_digit(d)
    d = get_unit_digit(e)
    # multiply the unit digits
    result = str(c * d)
    # if the product is negative, switch the digits again
    if result[-1] == '-':
        result = "0" + result[1:-1]
    return result
