
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
    # Part 1: Get the digits of a and b
    digit_a = sum(int(d) for d in str(a))
    digit_b = sum(int(d) for d in str(b))
    # Part 2: Multiply the digits of a and b
    product_digits = digit_a * digit_b
    # Part 3: Format the result as a string
    return ''.join(['{}{}'.format(d, b) if d != 0 else d for d in product_digits])
