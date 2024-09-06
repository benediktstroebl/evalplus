

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    i = 1
    while i * i < n:
        i += 1
    while i > 1:
        if n % i == 0:
            return i
        i -= 1
    else:
        return 1

