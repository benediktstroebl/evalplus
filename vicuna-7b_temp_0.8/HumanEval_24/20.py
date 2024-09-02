

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    while True:
        candidate = 2
        while candidate * candidate <= n:
            if n % candidate == 0:
                return candidate
            candidate += 1
        return n