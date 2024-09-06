

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while True:
        if a % b == 0:
            return b
        elif b % a == 0:
            return a
        else:
            a, b = b, a - b
    return 1