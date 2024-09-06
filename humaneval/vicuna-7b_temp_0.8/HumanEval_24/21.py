

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def _largest_divisor(n: int, r: int) -> int:
        """ Recursively find the largest divisor of n smaller than n, starting from r."""
        if r >= n:
            return r
        if n % r == 0:
            return r
        if r == 1:
            return n
        return _largest_divisor(n, r + 1)
    return _largest_divisor(n, 2)
