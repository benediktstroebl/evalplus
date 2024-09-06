

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    assert n > 1, 'Error: The input must be an integer greater than 1.'

    factor = 2
    while n % factor != 0:
        factor += 1

    largest_prime_factor = factor

    while n % factor == 0:
        n = n // factor
        factor += 1

    if n > largest_prime_factor:
        largest_prime_factor = n

    return largest_prime_factor
