

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n < 2:
        raise ValueError('n must be greater than 1')
    max_prime = n - 1
    while max_prime > 0:
        if max_prime % 2 == 0:
            max_prime = max_prime // 2
        else:
            if n % max_prime == 0:
                return max_prime
            else:
                max_prime -= 1
    return n
