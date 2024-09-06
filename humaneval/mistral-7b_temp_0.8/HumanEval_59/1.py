

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factors = [i for i in range(1, n + 1) if n % i == 0]
    for i in range(len(factors) - 1, 0, -1):
        if is_prime(factors[i]):
            return factors[i]

