

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('arguments must be integers')
    if a == 0 or b == 0:
        raise ValueError('arguments must not be zero')

    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a % b
    return a

