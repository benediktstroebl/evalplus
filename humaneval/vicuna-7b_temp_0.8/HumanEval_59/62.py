

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # first try to find the prime factor with the largest prime factorization
    # which is much faster than using a full prime decomposition
    candidate = 2
    max_candidate = n
    while candidate * candidate <= n:
        if n % candidate == 0:
            # if n has a factor of candidate, then it cannot be a prime
            max_candidate = candidate * 2
            candidate = 2
        else:
            candidate += 2
    # if we didn't find a prime factor larger than the square root of n
    # then there cannot be one, so return 1
    return max_candidate if max_candidate > sqrt(n) else 1
