

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Hint: Considering multiples of 2 from 2 up to sqrt(n) will not be enough.
    # Instead, start from the number's largest prime factor and keep searching.
    p = 2
    while p < int(n ** 0.5):
        if n % p == 0:
            return p
        else:
            p += 1
    if p ** 2 <= n:
        return p
    return 1

