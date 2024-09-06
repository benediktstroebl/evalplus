

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # base case
    if n < 2:
        return n
    # find the largest divisor
    max_divisor = max(largest_divisor(n // i) for i in range(2, n+1))
    return max_divisor