

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    m = 2
    while m <= n:
        if n % m == 0:
            return m
        m += 1
    return 1

