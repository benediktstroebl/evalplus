

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    a = min(a, b)
    while a > 0:
        if a <= b:
            temp = a
            a = b
            b = temp
        a -= b
    return a
