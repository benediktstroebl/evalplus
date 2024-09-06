

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    max_prime = 2
    while n % 2 == 0:
        n //= 2
    # n is now odd
    while n != 1 and max_prime < n:
        if n % max_prime == 0:
            n //= max_prime
        else:
            max_prime += 1
    return max_prime

