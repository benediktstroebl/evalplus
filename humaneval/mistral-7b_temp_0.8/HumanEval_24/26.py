

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 1:
        raise ValueError(f"n={n} must be a natural number")

    for i in range(1, n):
        if n % i == 0:
            return i

    return n

