
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
    # check if both numbers are negative
    if (a < 0) == (b < 0):
        a, b = -a, -b

    # check if the numbers are even or odd
    if a % 2 == 0:
        a = "0" + str(a)
    else:
        a = str(a)
    if b % 2 == 0:
        b = "0" + str(b)
    else:
        b = str(b)

    # Find the unit digits of both numbers
    ud_a = find_unit_digit(a)
    ud_b = find_unit_digit(b)

    # Check if the digits of the units match
    if ud_a[0] == ud_b[0]:
        ud_a_2 = str(ud_a[1]) + str(ud_a[2]) + str(ud_a[3])
        if ud_b[1:] == ud_a_2[1:]:
            product = "0"
            for i in range(len(ud_a_2)):
                if ud_a_2[i] == "1":
                    product += "1"
                else:
                    product += "0"
            return product

    # check if the numbers are odd or even
    if (a % 2 != 0) != (b % 2 != 0):
        return "0"

    # Check if the second number has a leading zero
    if b[0] == "0":
        b = b[1:]

    # Check if the product ends with a leading zero
    product = str(a * b)
    if product[-1] == "0" and len(product) > 1:
        product = "0" + product
    return product
