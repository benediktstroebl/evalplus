

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n < 2:
        return None
    while n % 2 == 0:
        n /= 2
    n = 3
    while n * n <= n:
        if n * n == n:
            return n
        if n % n == 0:
            n += 2
        else:
            n += 2
    return n
