

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factors = set()
    for i in range(2, n + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
        if not factors:
            break
    return factors.pop()

