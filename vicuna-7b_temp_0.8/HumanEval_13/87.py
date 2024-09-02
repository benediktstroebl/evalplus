

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Handle the case when a is 0
    if a == 0:
        return b
    
    # Handle the case when b is 0
    if b == 0:
        return 0
    
    # Check if a and b are relatively prime
    while a % b != 0:
        if a % a == b:
            return a
        a, b = b, a / b
    
    return a
