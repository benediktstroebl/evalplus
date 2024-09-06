

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    factors = []
    for factor in range(2, n):
        if n % factor == 0:
            factors.append(factor)
    largest_factor = factors[0]
    for num in factors:
        if is_prime(num) and num > largest_factor:
            largest_factor = num
    return largest_factor
