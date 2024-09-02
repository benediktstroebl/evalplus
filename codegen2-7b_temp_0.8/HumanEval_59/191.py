

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    max_factor = 1
    for factor in primes():
        if factor > n:
            break
        if n % factor == 0:
            max_factor = max(max_factor, factor)
    return
