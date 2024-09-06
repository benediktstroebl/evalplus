

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    a, b = int(a), int(b)

    if a == 0 or abs(a) < abs(b):
        a, b = b, a
    while a:
        a, b = b % a, a
    return b

