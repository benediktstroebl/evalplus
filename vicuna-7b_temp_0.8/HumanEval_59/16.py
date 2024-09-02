

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Base case: n < 2
    if n < 2:
        return 0
    # Check for prime
    if n > 2:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return i
        return n
    # Otherwise, n is a prime
    return n
