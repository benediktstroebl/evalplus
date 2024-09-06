

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 2
    # Start checking primes at 2 (smallest prime)
    # and increment by 1 each iteration.
    while i * i <= n:
        if n % i == 0:
            n = n // i
        else:
            i += 1
    return n

