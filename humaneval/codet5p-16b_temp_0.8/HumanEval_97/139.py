
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

    if a < 0 or b < 0:
        return 0
    
    a_units = a
    b_units = b
    result = 0
    count = 0
    while count <= 20:
        digits = a_units % 10
        a_units = a_units // 10
        result += digits
        digits = b_units % 10
        b_units = b_units // 10
        result += digits
        count += 1
    return result

