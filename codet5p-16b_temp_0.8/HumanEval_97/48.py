
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

    a_ = a
    b_ = b
    a = abs(a)
    b = abs(b)
    res = 0
    while a or b:
        if a >= 10:
            a -= 10
            res += b_ * a_
        else:
            b -= 10
        a_ = a
        b_ = b

    if a_ * b_ < 0:
        res *= -1
    return res

