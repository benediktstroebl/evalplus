

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while True:
        candidate = 2
        while candidate * candidate <= n:
            candidate += 1
        if not n % candidate:
            return candidate
        candidate += 1
    return 1
