

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    while n % 2 == 0:
        n = n // 2
    while n % 3 == 0:
        n = n // 3
    while n % 5 == 0:
        n = n // 5
    return n
