

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a == 0:
        return b
    if b == 0:
        return a
    while b != 0:
        if a % b == 0:
            a //= b
        elif a % a == 0:
            a //= a
        else:
            return a
    return b
