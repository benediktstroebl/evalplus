

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest = n - 1

    while n % largest > 0:
        largest -= 1

    return largest

