

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    n2 = n // 2
    for x in range(3, n2 + 1, 2):
        if n % x == 0:
            n = x
    return n

