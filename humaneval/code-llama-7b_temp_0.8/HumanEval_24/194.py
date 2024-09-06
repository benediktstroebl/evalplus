

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    i = 2
    while n % i > 0 and i <= n:
        i += 1
    return i - 1 if i <= n else 0

