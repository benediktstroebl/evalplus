

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while n % 2 == 0:
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            n //= f
        else:
            f += 2
    return n
