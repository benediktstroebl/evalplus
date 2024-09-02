

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n % 2 == 0:
        return 2
    i = n - 1
    while i > 0:
        if n % i == 0:
            large = i
        i -= 1
    return large
