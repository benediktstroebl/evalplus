

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    if n % 2 == 0:
        return 2
    i = 3
    while True:
        if n % i == 0:
            return i
        i += 2

