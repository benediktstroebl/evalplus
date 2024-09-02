

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_prime = 2
    while n % 2 == 0:
        n //= 2
        largest_prime = 2

    # n should always be odd at this point.
    # All prime numbers, except 2, are of the form 6k+1.
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n = n // i
    if n > largest_prime:
        largest_prime = n
    return largest_prime

