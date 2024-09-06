
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
    d_a = abs(a)
    d_b = abs(b)
    d_mul = 0
    for i in range(d_a, 0, -1):
        d_mul += i * d_b
    return d_mul
