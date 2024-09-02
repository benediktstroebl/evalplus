

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 1:
        return 1
    while n > 1:
        d = n // 2
        if n % d == 0:
            return d
        n = d
    return 1