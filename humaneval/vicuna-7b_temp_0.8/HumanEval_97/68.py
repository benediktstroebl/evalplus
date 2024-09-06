
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
    # Check for overflow
    if a >= 1000000000 or b >= 1000000000:
        return 0
    
    # Convert the input to base 10
    a_base10 = str(a)
    b_base10 = str(b)
    
    # Extract the unit digits
    a_unit_digits = [digit for digit in a_base10]
    b_unit_digits = [digit for digit in b_base10]
    
    # Merge the unit digits
    a_unit_digits_length = len(a_unit_digits)
    b_unit_digits_length = len(b_unit_digits)
    merged_unit_digits = [0] * (max(a_unit_digits_length, b_unit_digits_length) + 1)
    for i in range(min(a_unit_digits_length, b_unit_digits_length)):
        merged_unit_digits[i] = a_unit_digits[i] if a_unit_digits[i] != b_unit_digits[i] else b_unit_digits[i]
    
    # Add the merged unit digits and convert back to base 2
    product = 0
    for i in range(len(merged_unit_digits)):
        product = (product << 1) + merged_unit_digits[i]
    
    return product % 10
