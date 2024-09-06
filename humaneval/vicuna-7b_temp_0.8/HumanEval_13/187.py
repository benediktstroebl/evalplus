

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    result = a
    while a != 0:
        if b % a == 0:
            result = a
        else:
            b //= a
            a //= b
    return result