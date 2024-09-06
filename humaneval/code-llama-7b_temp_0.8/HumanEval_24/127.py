

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest = 0
    i = n
    while i > 0:
        if n % i == 0:
            largest = i
        i -= 1
    return largest

