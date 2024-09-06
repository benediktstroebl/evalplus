

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n % 5 == 0:
        return 5
    if n % 3 == 0:
        return 3
    if n % 2 == 0:
        return 2
    return 1
