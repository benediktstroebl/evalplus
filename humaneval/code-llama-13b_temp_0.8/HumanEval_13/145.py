

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a == 0 or b == 0:
        return max(a, b)
    if a < 0:
        a = abs(a)
    if b < 0:
        b = abs(b)
    while a % b != 0:
        a, b = b, a % b
    return b
