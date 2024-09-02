

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Search through n/2 to find the largest prime factor of n
    # and return the largest prime factor
    largest_prime = 1
    for i in range(n//2, 2, -1):
        if (n % i == 0) and is_prime(i):
            largest_prime = i
    return largest_prime

