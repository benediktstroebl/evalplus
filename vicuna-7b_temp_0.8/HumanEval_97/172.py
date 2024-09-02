
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
    a_units = str(a)
    b_units = str(b)
    product = 0
    if a_units[-1] == b_units[-1]:
        product = product * 10 + a_units[-1] * b_units.split("")[0]
    else:
        product = 0
    return product
