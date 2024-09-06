

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Bubble sort is too slow.
    #for x in range(n, 1, -1):
    #    if n % x == 0:
    #        return x
    #return 1

    # The following is a simple approach that uses the fact that n >= 1.
    # We're only interested in n/1, n/2, n/4, ..., 1, so we only need to check if
    # any of these numbers divide n.
    # The 1 is always a divisor but we need to make sure we don't divide by 0.
    for x in range(2, n+1):
        if n % x == 0:
            return x
    return 1
