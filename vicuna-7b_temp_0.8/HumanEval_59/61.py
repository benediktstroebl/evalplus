

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
    x = int(sqrt(n))
    while x % 2 == 0:
        x = int(x * x + n) // 2
    return x + 1
