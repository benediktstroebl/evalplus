

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    assert isinstance(n, int), f"n is not an int, got type {type(n)}"
    assert n > 0, f"n must be a positive int, got {n}"

    if n % 2 == 0:
        return n // 2
    return 3 * n + 1
