

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n == 2:
        return n
    elif n % 2 == 0:
        return 2
    res = 2
    i = 3
    while i * i < n:
        if n % i == 0:
            res = i
            n = n // i
        else:
            i += 2
    if i * i > n:
        return res
    return n

