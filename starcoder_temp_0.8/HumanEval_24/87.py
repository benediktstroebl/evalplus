

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    k = 2
    while k * k <= n:
        if n % k == 0:
            n = n // k
        else:
            k = k + 1
    return n
