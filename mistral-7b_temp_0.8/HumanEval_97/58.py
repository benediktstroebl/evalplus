
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
    # calculate the first unit digit
    first_unit_digit = a % 10
    # calculate the second unit digit
    second_unit_digit = b % 10
    # calculate the product
    product = first_unit_digit * second_unit_digit
    # return the product
    return product

