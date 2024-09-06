

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    f = 2
    while f ** 2 <= n:
        if n % f == 0:
            n //= f
        else:
            f += 1
    return n

