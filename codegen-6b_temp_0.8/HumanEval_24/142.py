

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    i = 2

    while i < n:
        if n % i == 0:
            break
        i += 1

    return i

