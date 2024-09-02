

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def factors(n: int):
        """Return all factors of n."""
        factors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                factors.append(n // i)
        return factors

    def is_prime(n: int):
        """Return whether n is prime or not."""
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = factors(n)
    return max(filter(is_prime, factors))

