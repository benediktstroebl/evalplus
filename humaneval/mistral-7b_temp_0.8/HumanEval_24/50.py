

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # loop from 1 to n
    for x in range(1, n + 1):
        # check if n % x is 0
        if n % x == 0:
            # if true, return x
            return x
