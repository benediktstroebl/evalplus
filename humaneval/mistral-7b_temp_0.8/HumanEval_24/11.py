

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # return max(range(1, n)) if n % max(range(1, n)) == 0 else -1
    i = 1
    while i < n:
        if n % i == 0:
            return i
        i += 1
    return -1

