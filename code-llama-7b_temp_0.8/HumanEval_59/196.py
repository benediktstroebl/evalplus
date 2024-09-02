

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # We only need to check up to the square root of n to find the largest
    # prime factor since larger factors must be a product of primes that
    # are less than the square root.

    max = 1

    i = 2
    while i <= n / i:
        if n % i == 0:
            n = n / i
            max = i
        else:
            i += 1

    return max

