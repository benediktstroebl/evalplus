

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    i = 1
    while i > 0:
        i = a % b
        if i > 0:
            a = b
            b = i
    return b

