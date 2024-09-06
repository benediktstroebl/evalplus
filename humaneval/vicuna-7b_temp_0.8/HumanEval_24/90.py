

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    while True:
        div = n // 2
        if div > n - 1:
            return n
        if div == n:
            return div
        n = div
