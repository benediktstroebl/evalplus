

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Determine the Mersenne prime of the next largest power of 2 that is less than n.
    p = 2
    while p**2 < n:
        p += 1
    # Initialize variables for the loop to find the largest prime factor.
    i = 2
    j = 2
    d = 2
    while j * j <= n:
        # Check for primality of d and handle it if it is prime and the largest factor so far.
        if d % 2 == 1 and d > p:
            if d > n / d:
                return d
            # d is not the largest prime factor, so continue with the loop.
        # Otherwise, check for divisibility of d by the next larger prime.
        else:
            if d % p == 0:
                return p
        d *= j
        j *= j
    return p