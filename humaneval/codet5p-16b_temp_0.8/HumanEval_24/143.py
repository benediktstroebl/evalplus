

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    if n == 1:
        return 1
    for d in range(2, int(n **.5) + 1):
        if n % d == 0:
            return d
    return n

