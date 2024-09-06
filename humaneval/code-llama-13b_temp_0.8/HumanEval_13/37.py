

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a == 0 and b == 0:
        return 1
    elif a == 0:
        return abs(b)
    elif b == 0:
        return abs(a)

    tmp: int
    if a < 0:
        a = abs(a)
    if b < 0:
        b = abs(b)

    while b != 0:
        tmp = b
        b = a % b
        a = tmp

    return a

