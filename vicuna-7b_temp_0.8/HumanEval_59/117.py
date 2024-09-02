

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Check that n is not prime
    if n > 1 and n % 2 == 0:
        return 2
    # Find the prime factors of n using trial division
    while True:
        # Check if n is divisible by any of the prime factors
        for p in prime_factors:
            if n % p == 0:
                break
        else:
            # If n is not divisible by any of the prime factors, it must have a largest prime factor
            return n
    # If n is divisible by one of the prime factors, find the largest prime factor
    largest_prime = max(prime_factors, key=lambda x: x[0] if x else None)
    return largest_prime
