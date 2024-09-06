

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Check if a and b are negative
    if a < 0 or b < 0:
        return -1

    # Check if a and b are not zero
    if a == 0 or b == 0:
        return -1

    # Compare a and b
    if a < b:
        return greatest_common_divisor(b, a)
    else:
        return greatest_common_divisor(a, b)
