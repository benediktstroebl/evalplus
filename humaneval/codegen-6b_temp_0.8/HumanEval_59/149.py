

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Get base prime
    _prime = 2
    while n != 1:
        if n % _prime == 0:
            n /= _prime
            factor = _prime
        else:
            _prime += 1
    return factor
