

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 3:
        return 2
    if n % 2 == 0:
        return 3
    if n == 3:
        return 2
    while True:
        d = (n - 1) // 2
        if d * d > n:
            break
        if d % 2 == 0:
            return d + 1
        n = d
    return n

largest_prime_factor = largest_prime_factor