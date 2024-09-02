

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # check if a and b are positive
    if a < 0 or b < 0:
        raise ValueError("a and b should be non-negative integers")

    # if a and b are not relatively prime, there is no greatest common divisor
    if (a % b != 0) or (b % a != 0):
        return -1
    
    # find the largest common divisor of a and b
    while b != 0:
        if b % a == 0:
            return a
        a, b = b, a - b
    
    # if b is the largest number, return b as the greatest common divisor
    return b
