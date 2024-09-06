

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    x, y = 1, n
    while y % x!= 0:
        x, y = y, x + y
    return
