

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    highest_divisor = 1
    i = 1
    while i < n:
        if n % i == 0:
            highest_divisor = i
        i += 1
    return highest_divisor

