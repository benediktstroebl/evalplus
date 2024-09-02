

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # if n is evenly divisible by 2 then just divide by 2
    if n % 2 == 0:
        return n // 2
    # we can't divide by two, so we must be odd. So start at 3 and check every odd number
    # to see if it is a divisor
    i = 3
    while i < n:
        if n % i == 0:
            # found a divisor, return it
            return n // i
        else:
            # move on to the next odd number
            i += 2

