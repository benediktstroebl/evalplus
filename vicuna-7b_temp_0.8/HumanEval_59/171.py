

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Factorize n, and return its largest prime factor
    if n <= 3:
        return 2
    if n % 2 == 0:
        return n / 2
    p = 5
    while p <= int(n ** 0.5):
        if n % p == 0:
            break
        p += 6
    return p + (1 if n % p == 1 else p)