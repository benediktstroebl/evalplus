

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while True:
        if n % 2 == 0:
            return 2
        d = n // 2
        if d * d > n:
            n = d
        else:
            break
    prime_factors = []
    p = 3
    while p < n:
        if n % p == 0:
            break
        prime_factors.append(p)
        n //= p
        p += 2
    if n > 1:
        prime_factors.append(n)
    return max(prime_factors)