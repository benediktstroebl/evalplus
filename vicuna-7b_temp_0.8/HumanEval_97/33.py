
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
    # Check if the input is valid
    if a < 0 or b < 0:
        return -1
    # Convert to binary
    a_bin = str(a)
    b_bin = str(b)
    # Multiply the unit digits
    if len(a_bin) > 1:
        return a_bin[0] * b_bin[0] + a_bin[1] * b_bin[1]
    else:
        return a_bin[0] * b_bin[0]
