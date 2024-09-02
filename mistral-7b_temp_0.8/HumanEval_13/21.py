

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a > b:
        min = b
    else:
        min = a

    for x in range(1, min+1):
        if (a % x == 0) and (b % x == 0):
            return x
