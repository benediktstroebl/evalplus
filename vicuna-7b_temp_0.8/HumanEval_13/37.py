

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    a, b = abs(a), abs(b)
    while a and b:
        if a < b:
            d = b
            b = a
            a = d
        else:
            d = a
            a = b
            b = d
    return a
