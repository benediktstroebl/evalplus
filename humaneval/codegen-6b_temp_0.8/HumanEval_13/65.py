

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # res = 1
    # while res > 0:
    #     res = a % b
    #     if res > 0:
    #         a = b
    #         b = res
    if a < b:
        a, b = b, a
    res = a % b
    while res > 0:
        a = b
        b = res
        res = a % b
    return b
