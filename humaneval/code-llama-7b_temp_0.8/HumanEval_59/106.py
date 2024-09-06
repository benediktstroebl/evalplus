

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Factor n by the closest prime numbers using sieve of Eratosthenes.
    factors = sieve_of_eratosthenes(n)

    # Find the largest prime number in the factor list.
    for i in reversed(range(1, len(factors))):
        if factors[i] is not None:
            return factors[i]

