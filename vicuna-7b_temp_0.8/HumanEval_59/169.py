

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Factors of 2 to n-1
    factors = [2]
    while n > 1:
        # Find the last factor
        for i in range(1, len(factors)):
            if factors[i] % n == 0:
                break
        n //= factors[i]
        del factors[i]

    # Find the largest prime factor
    largest_factor = 2
    for factor in factors:
        if factor > largest_factor:
            largest_factor = factor
    return largest_factor