
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

    a = abs(a)
    b = abs(b)

    a_digits = []
    b_digits = []

    while a:
        a, r = divmod(a, 10)
        a_digits.append(r)

    while b:
        b, r = divmod(b, 10)
        b_digits.append(r)

    product = 0

    for i, j in zip(a_digits, b_digits):
        product += i * j

    return product

