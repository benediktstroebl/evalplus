

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    d = 2
    while n % d != 0:
        d += 1
    res = d
    while n % d == 0:
        n //= d
    if n != 1:
        res = max(res, largest_prime_factor(n))
    return res

