
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
    if a < 0:
        pos_a = -1
    else:
        pos_a = 1

    if b < 0:
        pos_b = -1
    else:
        pos_b = 1

    a = abs(a)
    b = abs(b)

    m = 0
    for i in range(a):
        m += pos_b * (a % 10)

        a //= 10

    for i in range(b):
        m += pos_a * (b % 10)

        b //= 10

    return m

