

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Store the result and the remainder of the previous iteration
    result = a
    while b > 0:
        # If the remainder is zero, we have found a common divisor
        if b % a == 0:
            result = a
            a = b
            b = 0
        # Try the next number
        b = b // a
    # If the remainder is not zero, the result is a and b
    return result, b
