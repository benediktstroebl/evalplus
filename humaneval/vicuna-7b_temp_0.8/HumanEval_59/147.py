

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
    # Find the largest prime factor
    while True:
        # Find the largest prime that divides n - 1
        p = max(2, int(n ** 0.5 - 1))
        if n % p == 0:
            break
        n = p
    # Return the largest prime that divides n - 1
    return n - 1