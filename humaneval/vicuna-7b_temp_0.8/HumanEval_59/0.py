

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n <= 2:
        return n
    if n % 2:
        return largest_prime_factor(n // 2) * 3
    if n % 3:
        return largest_prime_factor(n // 3) * 2
    while True:
        d = n // 2
        if d * d > n:
            n = d
            break
        if d % 2 == 0:
            break
    return n
