
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
    
    positive = True
    if a < 0:
        a = -a
        positive = False
    if b < 0:
        b = -b
        positive = False

    a_unit = 0
    while a > 0:
        a_unit = a_unit + (a % 10)
        a = a // 10

    b_unit = 0
    while b > 0:
        b_unit = b_unit + (b % 10)
        b = b // 10

    if positive:
        return (a_unit * b_unit) % 10
    else:
        return (-1 * (a_unit * b_unit)) % 10

