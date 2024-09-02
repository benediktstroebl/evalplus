

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    p = 0
    while n % 2 == 0:
        n //= 2
        p += 1
    while n > 3:
        p = p + 1
        n //= n
    return p
