

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_prime = 1
    largest_prime_n = n
    d = 2
    while d * d <= largest_prime_n:
        while largest_prime_n % d == 0:
            largest_prime_n = largest_prime_n // d
            largest_prime = d
        d += 1
    if largest_prime_n > largest_prime:
        return largest_prime_n
    return largest_prime
