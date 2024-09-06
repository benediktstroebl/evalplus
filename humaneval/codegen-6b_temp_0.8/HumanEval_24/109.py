

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest = 1
    i = 1
    while n > 0:
        # Go up to the square root of n, until we can't go any higher.
        if n == i ** 2:
            return i

        i += 1
        # See if any i divides n. If not, try the next smallest value of i.
        if n % i == 0:
            largest = i
        n -= 1
    return largest

