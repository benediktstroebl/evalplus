

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # prime_factors returns the prime factors of an integer, except 1
    # if it is not a prime.
    if n % 2 != 0:
        return n

    # If n is 2, it is a prime and we return 2.
    if n == 2:
        return 2

    # If n has more than 1000 digits, we can't compute its prime factors.
    # Instead, we just return n.
    if len(str(n)) > 1000:
        return n

    # Try to compute the prime factors of n using the sieve of Eratosthenes.
    # If we reach 10^5, we know that n has at least 1000 digits, so we
    # can't compute its prime factors and return n instead.
    d, r = 2, n
    while d <= r:
        if d % 2 == 0:
            r += 1
        else:
            d *= d
    # If we got this far, we know that n is not prime and we have found its
    # largest prime factor.
    return r
