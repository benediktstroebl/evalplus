

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    d = 1
    while d * d <= n:
        if n % d == 0 and d >= n // d:
            return d
        d += 1
    return d -
