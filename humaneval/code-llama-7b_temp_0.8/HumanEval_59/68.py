

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # If n is a prime number, return it.
    if is_prime(n):
        return n

    # Find a prime factor.
    for i in range(n - 1, 1, -1):
        if n % i == 0 and is_prime(i):
            return i

