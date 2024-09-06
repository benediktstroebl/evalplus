def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    def is_prime(m):
        """Check if m is prime."""
        if m <= 1:
            return False
        for i in range(2, int(m**0.5) + 1):
            if m % i == 0:
                return False
        return True

    # Traverse through 2 and successive primes <= n, return the largest prime
    for i in range(2, n):
        if is_prime(i) and n % i == 0:
            return i
    return n