
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
    a = str(a)
    b = str(b)
    len_a = len(a)
    len_b = len(b)
    if len_a < len_b:
        len_b = len_a
    a = int(a[-len_b:])
    b = int(b[-len_b:])
    product = a * b
    return product

