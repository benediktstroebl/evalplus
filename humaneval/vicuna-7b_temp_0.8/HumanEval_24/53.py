

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 1:
        return 1
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    while True:
        if n % n // n == n // n % n == 0:
            n = n // n + 1
        else:
            return n
