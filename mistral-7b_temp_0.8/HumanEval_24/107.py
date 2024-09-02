

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    while n > 1:
        n -= 1
        if n > 0 and n % 2 == 0:
            return n
    return n
