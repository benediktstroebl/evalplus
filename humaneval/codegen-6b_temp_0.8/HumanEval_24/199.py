

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Using the property that d divides n if and only if d divides (n-d)
    # and n-d is even, so if n is d or bigger than d and (n-d) is even, then n is d
    for d in range(2, n):
        if n % d == 0:
            return d
    return n
