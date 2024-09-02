

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a == 0:
        return b
    elif b == 0:
        return a
    if a > b:
        a, b = b, a
    elif a == 0:
        return a
    while a != 0:
        if a == b:
            return a
        if b % a == 0:
            return a
        b %= a
        a, b = b, a
    return b
