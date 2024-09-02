

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    assert n >= 0
    if n < 2:
        return n

    lower, upper = 1, n
    while lower < upper:
        mid = (lower + upper) // 2
        if n % mid == 0:
            lower = mid + 1
        else:
            upper = mid
    return lower - 1
