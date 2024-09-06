

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2 or not n % 2 == 0:
        return 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            break
        p += 2
    return p
