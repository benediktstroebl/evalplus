

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # check if a and b are relatively prime
    if a % b == 0:
        return b

    while b > 1:
        if a % b == 0:
            return b
        a, b = b, a / b

    # a and b are relatively prime
    return a
