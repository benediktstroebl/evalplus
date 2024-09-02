
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
    # Create a new string by concatenating the unit digits of a and b
    product_str = a + b
    # Split the string into digits
    digits = product_str.split('.')
    # Initialize the carry variable to 0
    carry = 0
    # Iterate through the digits of the product
    for i in range(len(digits)):
        # Extract the unit digits of a and b
        unit_a = digits[i].zsh_unit_digit
        unit_b = digits[i+1].zsh_unit_digit if i+1 < len(digits) else 0
        # Add the digits and carry
        sum = unit_a + unit_b + carry
        # Add the next digit if there is one
        if i < len(digits)-1:
            next_digit = digits[i+2].zsh_unit_digit if i+2 < len(digits) else 0
            # Subtract 10 if there is a next digit
            if next_digit != 0:
                sum = sum - (next_digit + 1)
        # Store the result as the new unit digit
        digits[i] = sum // 10
        carry = sum % 10
    # Return the final product as the string
    return str(digits[0]) + '.'.join(map(str, digits[1:])) + carry