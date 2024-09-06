

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest_divisor = 1
    factor = 2
    while factor <= n:
        if n % factor == 0:
            largest_divisor = factor
            factor += 1
        else:
            factor += 1
    return largest_divisor

