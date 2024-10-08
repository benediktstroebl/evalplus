

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n <= 1:
        return n
    else:
        return largest_divisor(n - 1) if n % (n - 1) == 0 else largest_divisor(n - 1)

