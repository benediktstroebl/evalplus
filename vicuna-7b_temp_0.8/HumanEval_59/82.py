

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return 1
    if n % 2:
        return 2
    while True:
        d = n // 2
        if d == 1:
            break
        if d > 1 and d % 2 == 0:
            n = d
            continue
        if d > n:
            break
    while d > 1:
        d += 1
        if d == n:
            break
    return d
