

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    n_half = round(n / 2)
    for i in range(n_half, 0, -1):
        if n % i == 0:
            return i
    return 1

