

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Our first guess is that the largest prime factor is n // 2.
    candidate = n // 2

    # Check if n is divisible by candidate.
    if n % candidate == 0:
        return candidate

    # n is not divisible by candidate.
    # Now we need to find a new candidate.
    # A new candidate must be smaller than n // 2.
    candidate = candidate - 1

    # Keep reducing the candidate by 1 until we find the largest prime.
    while n % candidate != 0:
        # Remember to reduce candidate by 1 before you try a new one.
        candidate = candidate - 1

    return candidate

