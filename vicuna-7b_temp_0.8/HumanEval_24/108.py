

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n == 1:
        return 1
    else:
        candidate = n - 1
        while candidate % n == 0:
            candidate -= n
        return candidate
