

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while a != 0:
        if a % b == 0:
            return b
        a = a // b
        if b == 0:
            return 1
        b = b // 2
    return 1
