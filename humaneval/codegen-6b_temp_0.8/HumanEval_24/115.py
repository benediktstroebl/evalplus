

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisor = 0
    for div in range(1, n):
        if n % div == 0:
            divisor = div
    return divisor

