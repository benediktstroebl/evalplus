

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factors = []

    # We only need to go up to the square root of n
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            factors.append(i)

    # We can check all factors we found in one run
    for i in range(0, len(factors)):
        factor = factors[i]
        # If a factor is not prime, it has smaller factors.
        # We can remove it from the list of potential prime factors
        if is_prime(factor):
            continue

        for j in range(2, factor):
            if factor % j == 0:
                factors.remove(factor)
                break

    return max(factors)

