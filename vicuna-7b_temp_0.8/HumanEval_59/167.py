

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Check if n is prime
    if n > 1 and n % 2 == 0:
        return 2

    # Find the largest prime factor
    while True:
        # Try the trial division with the largest nontrivial known prime
        if n % 7 == 1:
            if n % 5 == 0:
                return 5
            if n % 7 == 0:
                return 7
        else:
            # Find the next largest prime
            p = 2
            while p * p <= n:
                p += 2
            p += 2
            # Check if the new prime is larger than the previous largest
            if p > n:
                return p
    return 2
