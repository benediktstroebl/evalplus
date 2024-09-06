

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    d = 1
    p = 2
    for i in range(1, int(n**0.5) + 1):
        d *= n
        r = d - 1
        if r % 2 == 0:
            break
    else:
        r = d
    while p < n and r % p == 0:
        r = r - p
    return r
