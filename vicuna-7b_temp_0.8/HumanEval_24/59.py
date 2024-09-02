

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    while True:
        remainder = n % i
        if remainder == 0:
            return i
        i += 1
    return n
