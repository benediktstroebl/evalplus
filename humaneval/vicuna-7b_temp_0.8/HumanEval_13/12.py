

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Check if b is 0, if so return a
    if b == 0:
        return a
    
    # Check if a and b have different signs
    if a < 0 != b < 0:
        return greatest_common_divisor(b, a)
    
    # Check if a and b are relatively prime
    while a % b != 0:
        a, b = b, a // b
    
    return a