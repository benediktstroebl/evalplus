

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    m = n - 1
    while m > 1:
        if m < 2:
            return 1
        if n % m == 0:
            return m
        m -= 1
    return n

