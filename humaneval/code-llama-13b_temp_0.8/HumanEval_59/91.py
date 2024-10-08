

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            prime_factors.append(i)
            n //= i
        i += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors[-1]

