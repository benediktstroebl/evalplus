

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # check if a and b are positive integers
    if a < 0 or b < 0:
        raise ValueError("a and b must be positive integers")
    # check if a is less than b
    if a < b:
        a, b = b, a
    # keep track of the maximum common divisor found so far
    max_common_divisor = 1
    while a != 0 and b != 0:
        # check if a and b are relatively prime
        if a % b == 0:
            break
        # increase the maximum common divisor
        max_common_divisor += b
        # divide a by b
        a, b = b, a
    # return the maximum common divisor
    return max_common_divisor