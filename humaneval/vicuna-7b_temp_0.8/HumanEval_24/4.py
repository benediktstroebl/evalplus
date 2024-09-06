

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    while True:
        divisor = int(round(n / 2))
        if divisor * 2 == n:
            return divisor
        n = n - divisor