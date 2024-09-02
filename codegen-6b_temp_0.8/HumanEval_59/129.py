

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n == 1:
        return 1
    pf = 2
    while n > 1:
        if n%2 == 0 and is_prime(n):
            return 2
        else:
            pf = n
            n = n/2
    return pf
