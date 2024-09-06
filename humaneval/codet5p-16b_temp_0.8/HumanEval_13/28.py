

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    if a > b:
        max_int = a
        min_int = b
    else:
        max_int = b
        min_int = a
    divisor = min_int
    while divisor!= 0:
        rest = max_int % divisor
        max_int = divisor
        divisor = rest
    return max_int

