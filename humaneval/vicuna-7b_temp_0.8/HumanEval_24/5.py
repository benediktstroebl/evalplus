

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    i, j = 1, n
    while j > 1:
        while j % i == 0:
            j = j / i
        i += 1
    return i
