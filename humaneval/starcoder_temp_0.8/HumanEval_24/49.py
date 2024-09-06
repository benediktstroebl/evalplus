

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n = n / factor
        else:
            factor += 1
    return n
