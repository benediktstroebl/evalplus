

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    largest_prime = n
    factor = 2
    while n % 2 == 0 and factor <= n / 2:
        if is_prime(factor):
            largest_prime = factor
        factor += 1

    factor = 3
    while factor <= largest_prime / 2:
        if n % factor == 0:
            if is_prime(factor):
                largest_prime = factor
        factor += 2
    return largest_prime

