

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a

    # euclidean algorithm for GCD
    while y != 0:
        a, b = b, a % b
    return a

