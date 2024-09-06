

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n % 2 == 0:
        return 2
    while True:
        d = n // 2
        if d * d > n:
            break
        n = d
        if d % 2 == 0:
            return d
    return 1