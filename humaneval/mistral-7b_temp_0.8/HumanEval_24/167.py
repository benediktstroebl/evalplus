

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # r1 is the remainder of n / r
    # r0 is the divisor, e.g. for 15 / 5, r0 is 5
    r0 = n
    r1 = n % r0
    while r1 != 0:
        r0 -= 1
        r1 = n % r0
    return r0

