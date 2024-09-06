def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Priority queue to store the factors. Pushing the smallest factor at first.
    pmax = float('-inf')
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
        if i > pmax:
            pmax = i
    # If n is a square number, the largest factor occurs twice.
    if len(factors) == 0:
        return pmax
    elif len(factors) == 1:
        return factors[0]
    else:
        return factors[-1]