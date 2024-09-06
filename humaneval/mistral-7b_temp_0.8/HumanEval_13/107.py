

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # x is a greatest common divisor of a and b
    if a == b:
        return a
    if a < b:
        a, b = b, a
    x = a % b
    if x == 0:
        return b
    return greatest_common_divisor(b, x)

