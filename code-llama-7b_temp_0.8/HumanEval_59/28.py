

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_prime = 2
    while n % 2 == 0:
        largest_prime = 2
        n //= 2
    i = 3
    while n != 1 and i <= n:
        while n % i == 0:
            largest_prime = i
            n //= i
        i += 2
    return largest_prime

