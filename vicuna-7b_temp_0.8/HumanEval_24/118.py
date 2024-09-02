

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    n = abs(n)
    while n > 1:
        d = 1
        while d <= n//d:
            d += 1
        n -= d * d
    return n