

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a == 0 or b == 0:
        return 0

    c = (a if a > b else b)
    while c > 0:
        if a % c == 0 and b % c == 0:
            return c

        c -= 1
    return 0
