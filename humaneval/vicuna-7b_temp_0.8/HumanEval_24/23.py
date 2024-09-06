

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    candidates = [2, 3, 4, 6, 7, 8, 9, 10, 12, 14, 15]
    result = 0
    while len(candidates) > 0:
        current = max(candidates)
        if n % current == 0:
            candidates.remove(current)
            result = max(result, current)
    return result
