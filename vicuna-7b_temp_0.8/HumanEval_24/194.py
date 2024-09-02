

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 2:
        return 1
    while n > 1:
        if n % 2 == 0:
            if n % 3 == 0:
                return n
            else:
                n = 3 * n + 1
        n = n - 1
    return n
