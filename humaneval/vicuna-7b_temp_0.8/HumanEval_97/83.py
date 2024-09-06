
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
    # Check if the input is a valid number
    if not (a > 0 and a < 1000000000 and b > 0 and b < 1000000000):
        return -1

    # Extract the unit digits of a and b
    a_units = sum(int(d) * (a // d) for d in str(a))
    b_units = sum(int(d) * (b // d) for d in str(b))

    # Calculate the product
    product = 0
    for i in range(a_units, len(a)):
        product = product * (10 - (a_units % 10)) + int(a_units % 10) * (10 - (b_units % 10)) + int(b_units % 10)
    if a_units > b_units:
        product *= 10

    # Return the product
    return product
