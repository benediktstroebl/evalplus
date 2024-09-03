def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    a, b = 0, 1
    while b <= n:
        a, b = b, a+b
    return a

