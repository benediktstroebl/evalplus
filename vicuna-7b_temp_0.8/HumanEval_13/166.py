

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Check if a is 0 or b is 0
    if a == 0 or b == 0:
        return 0

    # Calculate the Euclidean algorithm to find the GCD of a and b
    while b != 0:
        if a % b == 0:
            a, b = b, a % b

    return a