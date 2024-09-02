

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n == 2:
        return n
    prime_factors = []
    for i in range(2, n + 1):
        if not n % i:
            prime_factors.append(i)
    return prime_factors[-1
