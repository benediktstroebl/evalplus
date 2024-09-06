

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    x = 1
    while x <= n:
        if n % x == 0:
            return x
        x += 1
    return n
