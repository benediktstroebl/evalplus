

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factors = [2]
    while n > 1:
        for x in factors:
            if x % n == 0:
                break
        if x == n:
            return x
        n //= x
        factors = [y for y in factors if y != x]
    return n