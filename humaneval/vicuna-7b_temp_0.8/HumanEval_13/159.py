

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # divide a by b and store remainder in r
    remainder = a % b
    # if r is 0, b is the gcd
    if remainder == 0:
        return b
    # divide a by remainder and store quotient in q
    quotient = a // remainder
    # if quotient is 0, r is the gcd
    if quotient == 0:
        return remainder
    # return the gcd of r and q
    return greatest_common_divisor(remainder, quotient)
