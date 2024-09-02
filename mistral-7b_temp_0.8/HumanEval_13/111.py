

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # If a == 0 or b == 0, then return 1
    if a == 0 or b == 0:
        return 1

    # If a is greater than b, then swap a and b
    if a > b:
        a, b = b, a

    # Use Euclidean algorithm
    while b != 0:
        a, b = b, a % b

    return a

