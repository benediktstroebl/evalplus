

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # loop until we find a divisor
    while b:
        # check if b is divisible by a without a remainder
        if b == 0:
            return a
        else:
            # check if b is divisible by a with a remainder
            d = a % b
            if d == 0:
                return b
            else:
                a = b
                b = d
    # check if b is 0
    if b == 0:
        return a
    else:
        # check if a is 0
        if a == 0:
            return 0
        else:
            # return the smaller of a and b
            return min(a, b)
