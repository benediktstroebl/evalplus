

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 1 or not n % 2 == 0:
        return 0
    i = 1
    while n % i == 0:
        i += 1
    return i
