

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # check if a and b are positive
    if a < 0 or b < 0:
        return 0
    
    # if a and b are not positive, return 0
    while b != 0:
        if b % a == 0:
            return a
        a, b = b, a - b
    # if b reaches 0, return 1
    return 1
