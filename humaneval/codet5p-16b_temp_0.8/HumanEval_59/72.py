

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n < 2:
        raise ValueError('Input must be greater than 1')
    max_prime = 2
    i = 3
    while i <= n:
        if n % i == 0:
            max_prime = i
        i += 2
    return max_prime

