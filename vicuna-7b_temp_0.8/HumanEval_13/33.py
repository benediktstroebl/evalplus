

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Try two quick checks
    if a == 0:
        return b
    elif b == 0:
        return a

    # Try all possibilities
    for candidate in range(1, min(a + 1, b + 1) + 1):
        if (a % candidate == 0 and b % candidate == 0) or (a == candidate and b == 0):
            return candidate

    # If no common divisor found, return the largest of a and b
    return max(a, b)
