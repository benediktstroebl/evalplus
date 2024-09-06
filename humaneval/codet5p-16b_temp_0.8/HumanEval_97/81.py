
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

    a_unit = str(a)[::-1]
    b_unit = str(b)[::-1]
    product = int(a_unit[0])*int(b_unit[0])
    product += int(a_unit[1])*int(b_unit[1])
    return product
