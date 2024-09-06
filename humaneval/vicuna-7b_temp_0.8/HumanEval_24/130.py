

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n % 2 != 0:
        return n
    if n % 3 != 0:
        return 3
    for i in range(4, n):
        if n % i == 0:
            return i
    return n