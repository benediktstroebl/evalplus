

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    assert isinstance(n, int) and n > 0
    if n == 1:
        return n
    else:
        return largest_divisor(n // 2) if n % 2 == 0 else largest_divisor(n // 3)

