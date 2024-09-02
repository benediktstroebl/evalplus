

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    a_min = min(a, b)
    while True:
        if a_min == 0:
            return b
        a, b = a_min, b % a_min
