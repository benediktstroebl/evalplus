

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Find the largest prime factor up to n/2
    k = len(str(n)) - 1
    for p in primes[k:]:
        if n % p == 0:
            break
    else:
        # n is prime, so the largest prime factor is n itself
        return n
    while p * p <= n:
        p += 1
    return p
