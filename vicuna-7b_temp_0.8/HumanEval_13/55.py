

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Check for divisibility
    if a < 0 or b < 0:
        return 0
    if a % b == 0:
        return a
    while b > 0:
        if a % b == 0:
            a = b
            b = a - b
        else:
            b = b // a
    return b