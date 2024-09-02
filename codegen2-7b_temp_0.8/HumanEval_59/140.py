

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_factor = 1
    while prime_factor * prime_factor <= n:
        if n % prime_factor:
            prime_factor += 1
        else:
            n = n // prime_factor
    return prime
