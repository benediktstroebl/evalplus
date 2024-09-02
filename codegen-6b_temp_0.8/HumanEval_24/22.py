

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    assert n >= 0, "The number must be positive"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        candidate = n
        while candidate > 0:
            if n % candidate == 0:
                return candidate
            candidate -= 1

