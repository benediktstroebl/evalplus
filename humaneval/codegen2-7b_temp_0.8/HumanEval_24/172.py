

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for x in range(1, n):
        if n % x == 0 and x > n:
            return x
    return -1
