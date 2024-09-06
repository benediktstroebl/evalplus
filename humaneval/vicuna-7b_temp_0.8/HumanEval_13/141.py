

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Check for small cases
    if a == 0:
        return 0
    if b == 0:
        return 0
    if a % b == 0:
        return a
    # Check for larger cases
    while b > 1:
        if b % a == 0:
            return a
        a, b = b, a // b
    return a
