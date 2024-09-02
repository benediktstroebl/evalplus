

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    assert n > 1 and is_prime(n) == False
    m = 2
    while m * m <= n:
        if n % m == 0:
            n //= m
        else:
            m += 1
    return n
