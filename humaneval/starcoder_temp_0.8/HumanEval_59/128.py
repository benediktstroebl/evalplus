

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    assert n > 1 and is_prime(n) == False
    i = 2
    while i*i <= n:
        if n % i == 0:
            n = n // i
        else:
            i = i + 1
    return n

