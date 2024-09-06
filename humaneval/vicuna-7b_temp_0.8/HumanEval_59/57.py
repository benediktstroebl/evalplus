

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    n = int(n)
    if n < 2 or n % 2 == 0:
        return 2
    while True:
        d = n // 2
        if d * d > n:
            return d
        if d == 2:
            break
    r = n // d
    while r % 2 == 0:
        r = r // 2
    return r
