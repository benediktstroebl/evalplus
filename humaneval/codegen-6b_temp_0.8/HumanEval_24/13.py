

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    smallest = 1
    while (n % smallest) != 0:
        smallest += 1
    return smallest
