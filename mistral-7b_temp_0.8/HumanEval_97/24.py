
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

    # split the numbers into digits
    a_digits = [int(d) for d in str(a)]
    b_digits = [int(d) for d in str(b)]
    # multiply the digits together
    product = 1
    for a_digit in a_digits:
        for b_digit in b_digits:
            product *= (a_digit * b_digit) % 10
    # return the product
    return product
