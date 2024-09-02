

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n == 1:
        return 1
    else:
        while True:
            candidate = (n // 2) - 1
            if not n % candidate:
                return candidate
            n = n - candidate