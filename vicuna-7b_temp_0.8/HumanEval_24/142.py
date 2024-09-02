

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    candidates = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    while candidates:
        candidate = candidates[0]
        candidates.remove(candidate)
        if n % candidate == 0:
            return candidate
    return 0
