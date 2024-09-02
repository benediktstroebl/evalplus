

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_prime = 0
    for factor in range(1, n+1):
        if n % factor == 0:
            if is_prime(factor) and factor > largest_prime:
                largest_prime = factor
    return largest_prime

