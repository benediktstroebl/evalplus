

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # binary search
    while a != b:
        if a < b // 2:
            a, b = b, a + b // 2
        else:
            a, b = b, a - (b - a) // 2
    return a