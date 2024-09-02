

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a == b:
        return a
    elif a > b:
        a, b = b, a
    
    for factor in range(1, a + 1):
        if a % factor == 0 and b % factor == 0:
            return factor
    
    return 1
