

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        return 1
    while True:
        p = i
        for p_idx in range(i ** 2, int(n ** 0.5) + 1, i):
            if n % p_idx == 0:
                p = p_idx
                break
        if p < n:
            return p
    return 1
