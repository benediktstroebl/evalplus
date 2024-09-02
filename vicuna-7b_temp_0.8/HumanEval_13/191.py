

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # check for special case when b is 0
    if b == 0:
        return a
    
    # check for special case when a is 0
    if a == 0:
        return 0
    
    # check for special case when b is 1
    if b == 1:
        return a
    
    # use Euclidean algorithm
    while a != 0 and b != 0:
        if a % b == 0:
            d, r = b, a
            a, b = r, d
        else:
            d, r = a, b
            a, b = r, d
    
    return d