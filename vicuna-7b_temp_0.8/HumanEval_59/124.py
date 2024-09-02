

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Check if n is a prime
    if n == 1 or n % 2 == 0:
        return 1
    # Check for composite numbers
    while True:
        # Check if n is a prime
        if n == 1 or n % 2 == 0:
            return 1
        # Check for composite numbers
        if n % 2 == 0:
            n = 2 * n + 1
        else:
            n = n - 1
    # None of the above cases work, so n must be a prime
    return n
