

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n == 0: return 0
    if n == 1: return 1
    d = 2
    while d*d <= n:
        if n%d == 0: n //= d
        else: d += 1
    return n
