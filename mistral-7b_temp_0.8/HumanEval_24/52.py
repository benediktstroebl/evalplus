

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 1:
        raise ValueError("Number must be positive")
    i = 1
    while i < n:
        if n % i == 0:
            return i
        i += 1
    return n
