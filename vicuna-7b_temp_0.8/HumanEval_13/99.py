

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while True:
        if b == 0:
            return a
        elif a % b == 0:
            return b
        else:
            a, b = b, a % b
