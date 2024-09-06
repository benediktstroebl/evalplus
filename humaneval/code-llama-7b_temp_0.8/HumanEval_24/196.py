

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 2:
        return n
    if n == 2:
        return 2
    if n % 2 == 0:
        return 2
    div = 3
    while div <= n:
        if n % div == 0:
            return div
        div += 2
    return n
