

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    while i ** 2 <= n:
        if n % i == 0:
            return i
        if n % (i+2) == 0:
            return i + 2
        i += 6
    return n

