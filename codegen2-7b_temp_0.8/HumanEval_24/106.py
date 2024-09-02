

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    max_factor = 2
    while n % max_factor!= 0:
        max_factor += 1
    return max_factor

