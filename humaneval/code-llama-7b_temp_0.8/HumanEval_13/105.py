

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b should be integers")
    if not a or not b:
        raise ValueError("a and b should be positive integers")

    if a < 0:
        a = abs(a)
    if b < 0:
        b = abs(b)

    while a != b:
        if a < b:
            a, b = b, a
        a = a - b

    return a

