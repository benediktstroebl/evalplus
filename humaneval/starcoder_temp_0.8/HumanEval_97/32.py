
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
    a, b = str(a), str(b)
    digit_a, digit_b = [int(n) for n in a], [int(n) for n in b]
    return int(''.join(str(d) for d in digit_a*digit_b))
