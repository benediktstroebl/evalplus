

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return 1
    while True:
        if n % 2 == 0:
            n = n / 2
            continue
        if n % 3 == 0:
            n = 3 * n / 3
            continue
        d = 5
        while d * d <= n:
            if n % d == 0:
                n = n / d
                d = (d * d) % n
                continue
        return d
