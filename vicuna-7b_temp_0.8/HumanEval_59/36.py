

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return 1
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    while True:
        d = n // 2
        if d > 1:
            n = d
            continue
        if d % 2 == 1:
            n = d
            continue
        if d == 2:
            return d
        n = d + 1
