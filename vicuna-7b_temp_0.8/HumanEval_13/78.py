

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # base case
    if a < b:
        return 0
    
    # find the gcd of the remaining numbers
    a, b = b, a%b
    while a > 0:
        a, b = b, a//b
    
    return b
