

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    i = 2
    d = 1
    while n % i == 0:
        d *= i
        i += 2
    return d