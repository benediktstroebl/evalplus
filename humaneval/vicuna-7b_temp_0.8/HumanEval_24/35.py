

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    n = max(int(n), 1)
    d = 1
    while d <= n // d:
        d += 1
    return d
