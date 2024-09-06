

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest_divisor = n - 1
    while largest_divisor > 1 and n % largest_divisor > 0:
        largest_divisor -= 1
    return largest_divisor

