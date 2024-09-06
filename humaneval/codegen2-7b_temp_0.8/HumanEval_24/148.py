

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    return reduce(lambda x, y: y if x%y == 0 else x, range(1, n+1), 1)
