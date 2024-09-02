

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    return 1 if n % 2 == 0 else n if n % 3 == 0 else n if n % 5 == 0 else n if n % 7 == 0 else n % 11 == 0 else
