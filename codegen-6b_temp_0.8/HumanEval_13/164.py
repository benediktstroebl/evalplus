

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    gcd = 1
    while gcd > 0:
        result = a % b
        a = b
        b = result
        if a != 0:
            gcd = a
    return gcd

