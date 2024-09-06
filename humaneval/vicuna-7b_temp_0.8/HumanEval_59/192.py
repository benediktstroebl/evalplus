

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Use a hashset to avoid repeatedly computing the same prime factors
    factors = {1}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
        for j in range(i, int(n ** 0.5) + 1):
            if j not in factors and (j, i) not in factors:
                factors.add(j * i)
    return factors.pop()