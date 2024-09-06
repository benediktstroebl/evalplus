

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    n = abs(n)
    if n < 1:
        return n
    for i in range(2, n + 1):
        if n % i == 0:
            return i
    return n

