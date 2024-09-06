

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 3:
        return n
    if n % 2 == 0:
        return 2
    s = 3
    while s <= sqrt(n):
        if n % s == 0:
            n = int(n / s)
            s = 3
        else:
            s += 6
    return n
