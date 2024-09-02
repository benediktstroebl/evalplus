
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
    str_a = str(a)
    str_b = str(b)
    a = int(str_a[len(str_a) - 1])
    b = int(str_b[len(str_b) - 1])
    return a * b
