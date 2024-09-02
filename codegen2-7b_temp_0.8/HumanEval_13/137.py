

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a < b:
        a, b = b, a
    c = a % b
    while c!= 0:
        a = b
        b = c
        c = a % b
    return b
