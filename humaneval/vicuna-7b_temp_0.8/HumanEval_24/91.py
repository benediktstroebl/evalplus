

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def _largest_divisor_helper(m: int, n: int) -> int:
        if n % m == 0:
            return m
        while n > m:
            m += 1
        return m

    return _largest_divisor_helper(2, n)
