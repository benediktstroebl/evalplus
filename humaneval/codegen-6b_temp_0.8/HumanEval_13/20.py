

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b != 0:
        # if a bigger number than b is divided by b, then this can be updated
        # otherwise, the algorithm will keep scanning the iteration instructions
        # until one of the numbers become 0.
        t = b
        b = a % b
        # the operation to be performed every time the two numbers are
        # divided by each other
        a = t

    return a

