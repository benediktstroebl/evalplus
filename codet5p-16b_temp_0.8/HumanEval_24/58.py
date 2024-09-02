

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    n = abs(n)
    if n < 4:
        return n
    i = 2
    while i * i < n:
        i += 1
    return i if (n % i == 0) else n

