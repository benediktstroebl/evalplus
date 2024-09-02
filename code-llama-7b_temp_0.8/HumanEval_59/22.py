

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n == 2:
        return n
    for x in range(3, n // 2 + 1, 2):
        if n % x == 0 and is_prime(x):
            return x
    return n

