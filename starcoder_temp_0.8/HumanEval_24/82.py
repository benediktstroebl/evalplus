

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    if n % 2 == 0:
        return n//2

    largest_odd = n // 2
    while True:
        if n % largest_odd == 0:
            return largest_odd

        largest_odd -= 2
