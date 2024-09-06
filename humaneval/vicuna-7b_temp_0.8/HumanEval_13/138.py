

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Use Euclid's algorithm
    while b != 0:
        # If b is not a factor of a, we have found a
        if b % a == 0:
            return a
        # Otherwise, b must be the greatest common divisor
        a, b = b, a % b
    return b