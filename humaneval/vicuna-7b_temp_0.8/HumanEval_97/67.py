
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
    # Check if the product of the two input digits is 0
    if a % 10 != 0 or b % 10 != 0:
        # Convert the digits to base 10 and take the product
        product = sum([a_digit * b_digit for a_digit, b_digit in zip(str(a), str(b))])
        # Convert the product back to base 2
        return str(product)[2:]
    else:
        # If the product is 0, return 0
        return 0
