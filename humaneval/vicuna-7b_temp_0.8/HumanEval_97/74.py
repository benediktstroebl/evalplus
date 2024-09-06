
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
    # Create a helper variable to keep track of the current unit digit
    current_unit_digit = 0
    # Start from the rightmost digit and work left
    for i in reversed(range(len(str(a)))):
        # Multiply the current digit with the appropriate power of 10
        product = (int(str(a)[i]) * 10) + int(str(b)[i])
        # Add the current unit digit to the product
        product += current_unit_digit
        # Update the current unit digit
        current_unit_digit = (product % 10)
        # Clear the carry
        product = product // 10
    return str(a) + str(b)[::-1] + current_unit_digit
