
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

    result = 0
    a_positive = a > 0
    b_positive = b > 0
    
    if a_positive:
        a_unit_digit = a % 10
    else:
        a_unit_digit = -(-a % 10)

    if b_positive:
        b_unit_digit = b % 10
    else:
        b_unit_digit = -(-b % 10)

    result = a_unit_digit * b_unit_digit

    return result
