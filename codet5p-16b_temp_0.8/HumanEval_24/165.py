

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    from math import sqrt
    divisor = 1
    while divisor * divisor < n:
        divisor += 1
    return divisor if divisor * divisor == n else sqrt(n)

