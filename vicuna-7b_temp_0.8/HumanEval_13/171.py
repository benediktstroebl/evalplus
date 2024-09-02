

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a < 0 or b < 0:
        raise ValueError("Both arguments must be non-negative")
    if a == 0:
        return b
    if b == 0:
        return a
    while b:
        if a % b == 0:
            return max(a, b)
        a, b = b, a // b
    return a
