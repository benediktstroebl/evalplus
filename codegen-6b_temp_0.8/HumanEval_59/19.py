

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    assert n > 1
    if n == 1:
        return 1
    max_divisor = n // 2
    p = 2
    while p <= max_divisor:
        if n % p == 0:
            return p
        else:
            p += 1
    return n

