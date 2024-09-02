

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factors = []
    k = n
    while k % 2 == 0:
        k /= 2
        factors.append(2)

    for i in range(3, int(n ** 0.5) + 1, 2):
        while k % i == 0:
            k /= i
            factors.append(int(i))

    if k > 2:
        factors.append(int(k))
    return max(factors)

