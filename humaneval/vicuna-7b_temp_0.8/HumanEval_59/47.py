

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Find the largest prime p such that 2 <= p < n.
    p = 2
    max_i = 0
    while True:
        if n % p == 0:
            break
        p = p + 2
        if p > n:
            break
        max_i = i
    if max_i == 0:
        return 1
    else:
        return (p - 1) ** (max_i - 1)
