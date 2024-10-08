

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_factors = []
    x = n
    i = 2
    while x >= i:
        if n % i == 0:
            n = n // i
            prime_factors.append(i)
        else:
            i += 1
    return max(prime_factors)
