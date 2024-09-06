
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
    # First convert both numbers to strings
    a_str = str(a)
    b_str = str(b)
    # Remove the last digit from both strings
    a_str = a_str[:-1]
    b_str = b_str[:-1]
    # Get the unit digits of the strings
    a_unit_digits = [int(d) for d in a_str[1:].split('')]
    b_unit_digits = [int(d) for d in b_str[1:].split('')]
    # Get the result
    result = 0
    for i in range(0, min(len(a_unit_digits), len(b_unit_digits))):
        # Multiply the corresponding digits
        result = (result * 10) + a_unit_digits[i] * b_unit_digits[i]
    return result
