

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_prime = None
    i = 2
    while n > 1:
        while not is_prime(i):
            i += 1
        largest_prime = i
        n //= i
        i += 1
    return largest_prime

