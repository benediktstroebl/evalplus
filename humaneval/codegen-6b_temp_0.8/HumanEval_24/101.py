

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest = 1
    factor = 2
    while factor < n:
        if n % factor == 0:
            largest = factor
        factor += 1
    return largest

