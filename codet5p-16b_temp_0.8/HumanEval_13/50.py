

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    if a == 0 or b == 0:
        return max(a, b)
    if a == b:
        return a
    else:
        return greatest_common_divisor(min(a, b), max(a, b) % min(a, b))

