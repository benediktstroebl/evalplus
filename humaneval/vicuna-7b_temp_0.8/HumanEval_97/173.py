
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
    # Check if the two numbers are negative
    if a < 0 and b < 0:
        return -multiply(-a, -b)
    # Convert the numbers to strings
    a_str = str(a)
    b_str = str(b)
    # Extract the unit digits
    a_unit_digits = [int(digit) for digit in a_str if digit in '01']
    b_unit_digits = [int(digit) for digit in b_str if digit in '01']
    # Combine the unit digits
    product_unit_digits = [a_unit_digits[i] * b_unit_digits[i] for i in range(len(a_unit_digits))]
    # Add the remaining digits
    product_str = ''.join([int(digit) * (10 - sum(product_unit_digits)) for digit in str(a) if digit not in '01'] + [int(digit) * (10 - sum(product_unit_digits)) for digit in str(b) if digit not in '01'])
    return int(product_str)
