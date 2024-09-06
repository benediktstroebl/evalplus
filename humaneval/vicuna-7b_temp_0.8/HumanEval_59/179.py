

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Get the prime factors of n.
    p = 2
    while p <= n // p:
        n //= p
        p += 1
    if n % 2 == 0:
        return 2
    else:
        return n - 2
