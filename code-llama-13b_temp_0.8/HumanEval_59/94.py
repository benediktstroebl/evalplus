

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    i = 3
    while n != 1:
        if n % i == 0:
            factors.add(i)
            n //= i
        else:
            i += 2
    if len(factors) == 0:
        return None
    return max(factors)

