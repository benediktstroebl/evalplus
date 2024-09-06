

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a < b:
        a, b = b, a
    x, y = a, b
    while a % b != 0 or b % a != 0:
        if b < a:
            x, y = y, x
        else:
            x, y = a, b
        a, b = b, a % b
    return a