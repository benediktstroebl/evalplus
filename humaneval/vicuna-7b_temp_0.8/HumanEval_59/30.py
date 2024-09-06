

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    p, q, r = divmod(n, 2)
    while (p-q) % 2 != 0:
        p, q = q+p, p
    return p
