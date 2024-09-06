

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(n: int) -> bool:
        """Return True if n is a prime, False if n is not prime."""
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def factor(n: int) -> list:
        """Return a list of all prime factors of n."""
        factors = []
        for i in range(2, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors

    factors = factor(n)
    prime_factors = []
    for factor in factors:
        if is_prime(factor):
            prime_factors.append(factor)

    return max(prime_factors)
