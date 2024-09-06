

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Check if n is a prime
    if n > 1 and n % 2 == 0:
        return 2
    # Check if n is a power of 2
    if n == 2**k for k in range(len(str(n))):
        return 2**(len(str(n)) - 1)
    # Find the largest prime factor
    factors = Factors(n)
    max_factor = n
    for factor in factors:
        if factor > max_factor:
            max_factor = factor
    return max_factor
