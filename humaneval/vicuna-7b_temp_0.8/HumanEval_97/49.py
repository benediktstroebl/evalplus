
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
    # split the input
    a, b = int(a), int(b)
    # get the units digit of a and b separately
    a_unit_digits = get_unit_digits(a)
    b_unit_digits = get_unit_digits(b)
    # carry = 0
    carry = 0
    # add a and b and update the carry
    result = 0
    while a_unit_digits or b_unit_digits:
        if (a_unit_digits or b_unit_digits) and (a_unit_digits % 10 != b_unit_digits % 10):
            # if the carry is non-zero, add it to the result
            result = carry + (a_unit_digits * b_unit_digits // 10) % 10
            carry = (a_unit_digits * b_unit_digits // 10) % 10
        a_unit_digits = int(a_unit_digits / 10)
        b_unit_digits = int(b_unit_digits / 10)
    # add the last digit of the result and update the carry
    result = result + (a_unit_digits * b_unit_digits % 10) + carry
    # return the result
    return result
