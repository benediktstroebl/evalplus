
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
    # handle the case where the product is 0
    if a % 10 == 0 and b % 10 == 0:
        return 0
    # handle the case where one of the numbers is negative
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    # convert the input to 3 digits and take the last two digits of the product
    a = str(abs(a))[-3:]
    b = str(abs(b))[-3:]
    # get the units digit of the product by taking the last digit of the last two digits of the product
    prod_units = int(a*b[-1])
    # multiply the units digits of a and b
    prod_units_a = int(a[-1])
    prod_units_b = int(b[-1])
    product = prod_units*prod_units_a*prod_units_b
    # check if the product is 0
    if product == 0:
        return 0
    # convert the product back to 2 digits
    product = str(product)[:-3]
    # return the product
    return product
