
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
    a_units = a % 10
    a_tens = a // 10
    b_units = b % 10
    b_tens = b // 10

    return (a_units * b_units) + (a_units * b_tens) + (a_tens * b_units)
