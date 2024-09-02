

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    assert n > 1 and n % 2 != 0, 'n must be greater than 1 and odd'
    i = 3
    while n > i:
        if n % i == 0:
            n //= i
        else:
            i += 2
    return n

