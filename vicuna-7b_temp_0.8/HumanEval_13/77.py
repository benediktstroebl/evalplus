

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Check if b is not equal to 0
    if b != 0:
        # If b is greater, return it
        if b > a:
            return b
        # If a is greater, subtract it from b until b becomes 0
        while a > 0:
            b //= a
            a //= a
    # If a is greater, return a
    else:
        return a