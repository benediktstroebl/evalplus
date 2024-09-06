

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    all_factors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            all_factors.append(i)

    all_factors.append(n)
    all_factors.sort()
    all_factors.reverse()
    for factor in all_factors:
        if is_prime(factor):
            return factor

