

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Try to find a prime that divides n
    while True:
        if not n % 2:
            # If n is even, it cannot have any prime factors
            return 1
        d = 3
        while d * d <= n:
            # Keep trying factors until we find one that doesn't work
            while d * d <= n:
                if d * d > n:
                    break
                d *= d
            else:
                break
        # Otherwise, the next largest prime factor is d
        return d
