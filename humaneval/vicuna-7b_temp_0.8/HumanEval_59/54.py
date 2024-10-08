

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factors = []
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            continue
        for i in range(3, int(n ** 0.5) + 1, 3):
            if n % i == 0:
                n = i
                continue
        factors.append(n)
        n = n - 1
    return factors[-1]
