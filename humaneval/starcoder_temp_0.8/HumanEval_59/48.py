

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n % 2 == 0:
        return 2
    prime_factors = [2]
    i = 3
    while i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n = n / i
        else:
            i = i + 2
    return max(prime_factors)
