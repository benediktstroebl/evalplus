

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    assert n > 1
    if n % 2 == 0:
        div = 3
    else:
        div = 2
    while div < n:
        if n % div == 0:
            return div
        div += 2
    return n

