

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    while True:
        if n % 2 == 0:
            return n // 2
        if n % 3 == 0:
            return n // 3
        n = n - 1
        if n > 1:
            n = n // 2
    return None