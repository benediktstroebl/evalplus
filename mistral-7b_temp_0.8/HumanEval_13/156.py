

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a < 0 or b < 0:
        raise ValueError("a and b should be positive integers")
    if a == 0 or b == 0:
        return 0
    while b != 0:
        if a < b:
            a, b = b, a
        a = a % b
    return a

