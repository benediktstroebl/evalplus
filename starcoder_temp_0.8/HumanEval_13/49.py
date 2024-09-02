

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # for every pair (a, b) from this subset of numbers, check if there is no remainder
    # for such numbers, the pair is a greatest common divisor
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

    # if no pair of numbers exists for which no remainder exists, then a common divisor does not exist
    return 0

