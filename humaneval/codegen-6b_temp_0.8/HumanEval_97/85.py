
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
    # convert to strings to avoid '<' operations below
    a = str(a)
    b = str(b)

    # get product of input digits as strings
    product = ''
    for (i, num) in enumerate(a):
        product += str(int(a[i]) * int(b[i]))

    # convert back to int in integer arithmetic
    return int(product)

