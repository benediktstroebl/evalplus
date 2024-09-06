

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Return 0 if a or b is 0
    if a == 0 or b == 0:
        return 0
    
    # Check if a is divisible by b
    if a % b == 0:
        return a
    
    # If not, check if b is divisible by a
    return greatest_common_divisor(b, a % b)