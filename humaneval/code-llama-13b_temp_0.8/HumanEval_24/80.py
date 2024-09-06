

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    # determine if n is even or odd
    if n % 2 == 0:
        # check if 2 divides n evenly
        if n % 2 == 0:
            # return 2
            return 2
    else:
        # check if 3 divides n evenly
        if n % 3 == 0:
            # return 3
            return 3
        else:
            # n is odd and 3 does not divide n evenly
            return 1

