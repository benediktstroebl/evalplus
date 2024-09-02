

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # base case
    if a == 0:
        return b
    elif b == 0:
        return a

    # find the smallest number that is greater than or equal to both a and b
    if a >= b:
        c = a
    else:
        c = b

    # while the current number is not a prime
    while not is_prime(c):
        # divide the current number by the smallest number that is greater than or equal to both a and b
        d = divisors(c)[0]
        c = int(c / d)

    # return the smallest number that is greater than or equal to both a and b
    return c
