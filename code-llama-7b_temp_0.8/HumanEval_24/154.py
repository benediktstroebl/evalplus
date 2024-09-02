

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Fill this in.
    # let's call it d
    # check for d
    # if d evenly divides n
    # keep going
    # find out which number is less than n
    # that is evenly divisible by n
    # call it d
    # return d

    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i

