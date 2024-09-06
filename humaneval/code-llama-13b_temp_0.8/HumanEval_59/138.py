

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_factor = 1
    p = 2
    while p <= n // p:
        if n % p == 0:
            prime_factor = p
            n //= p
        else:
            p += 1
    if prime_factor < n:
        prime_factor = n
    return prime_factor
