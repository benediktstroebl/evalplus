
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
    a_inv = 10
    b_inv = 10
    for i in range(0, len(str(a))):
        a_inv *= int(str(a)[i])
    for i in range(0, len(str(b))):
        b_inv *= int(str(b)[i])
    return a_inv * b_inv
