

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    assert n > 1, "Invalid input"
    # We have already found the largest prime factor of 2, so we can start
    # searching at 3.
    factor = 3
    # Repeat until we find a factor that is less than n.
    while n >= factor * factor:
        # If n is divisible by factor, then factor is a factor of n.
        if n % factor == 0:
            # Update n to the quotient.
            n = n // factor
        else:
            # If n is not divisible by factor, increment factor by 2.
            factor += 2
    # At this point, n is a prime number.
    return n
