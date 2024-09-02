

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    return max(range(1, n + 1), lambda x: n % x if x <= n // x else x)
