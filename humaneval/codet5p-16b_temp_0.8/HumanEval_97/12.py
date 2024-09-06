
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

    def multiply_unit_digits(a_unit_digit, b_unit_digit):
        if a_unit_digit == 0 or b_unit_digit == 0:
            return 0
        else:
            return (a_unit_digit * b_unit_digit) % 10

    if a < 0 or b < 0:
        return -1
    else:
        product = 0
        for i in range(0, len(str(a))):
            product += multiply_unit_digits(int(str(a)[i]), int(str(b)[i]))
        return product
