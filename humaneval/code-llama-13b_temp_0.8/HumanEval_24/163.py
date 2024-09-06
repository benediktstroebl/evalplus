

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # return _largest_divisor(n, 2)
    return _largest_divisor_range(n, 2, 1)

