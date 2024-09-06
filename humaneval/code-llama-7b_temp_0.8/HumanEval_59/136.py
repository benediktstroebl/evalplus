

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # The loop tests factors from 2 (inclusive) to n (exclusive).
    for factor in range(2, n):
        # See if this is a factor of n.
        if n % factor == 0:
            # If so, see if n is also a factor of the current factor,
            # and if so return the largest.
            if largest_prime_factor(factor) > largest_prime_factor(n // factor):
                return factor
            else:
                return n // factor
    # If the largest factor found was 1, then return n as it is prime.
    return n
