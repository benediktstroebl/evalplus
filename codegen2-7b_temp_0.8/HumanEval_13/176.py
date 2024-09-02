

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a < b:
        greatest, lesser = a, b
    else:
        greatest, lesser = b, a
    while lesser!= 0:
        greatest, lesser = lesser, greater % lesser
    return
