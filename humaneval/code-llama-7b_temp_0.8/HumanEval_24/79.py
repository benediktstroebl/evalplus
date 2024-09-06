

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    m = n
    while m > 1:
        if n % m == 0:
            return m
        else:
            m = m - 1
    return 1
