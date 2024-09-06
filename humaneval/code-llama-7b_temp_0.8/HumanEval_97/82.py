
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

    # Convert to Str
    str_a = str(a)
    str_b = str(b)

    # Get Unit Digit
    unit_a = str_a[-1]
    unit_b = str_b[-1]

    # Multiply
    return int(unit_a) * int(unit_b)
