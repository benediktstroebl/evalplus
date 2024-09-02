

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 3:
        return 2
    n_copy = int(n)
    if n_copy % 2 == 0:
        return 2
    p = 3
    while True:
        p_copy = p
        while p_copy % 2 == 0:
            p_copy = p_copy + 1
        if p_copy > n_copy:
            break
        if p_copy not in prime_factors:
            break
    return max(prime_factors[p_copy - 1], p)
