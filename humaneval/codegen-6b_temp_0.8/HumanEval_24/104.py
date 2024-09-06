

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    l, r = 1, n
    while l <= r:
        m = (l + r) // 2
        if n % m == 0:
            return m
        elif m < n:
            l = m + 1
        else:
            r = m - 1
    return l
