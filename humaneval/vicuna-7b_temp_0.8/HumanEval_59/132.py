

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n <= 1:
        return n
    if n % 2:
        return n - 1
    p = 10000001
    while p <= n:
        if n % p:
            p = p + 1
        else:
            n //= p
    return n