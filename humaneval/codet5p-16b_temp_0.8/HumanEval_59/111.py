

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    largest_prime_factor = n
    i = 2
    while i <= largest_prime_factor:
        if largest_prime_factor % i == 0:
            largest_prime_factor = largest_prime_factor / i
        else:
            i += 1
    return int(largest_prime_factor)
