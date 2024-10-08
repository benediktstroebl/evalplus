

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    for x in range(n//2, 1, -1):
        if n % x == 0:
            return x
    return 1

