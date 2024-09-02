

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b
    """
    while b != 0:
        if a % b == 0 and b % a == 0:
            return a
        a, b = b, a % b
    """
    if a == 0:
        return b
    elif b == 0:
        return a
    return 0
