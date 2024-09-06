

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest_divisor = 1
    for n_d in range(2, n // 2 + 1):
        if n % n_d == 0:
            largest_divisor = n_d
    return largest_divisor

