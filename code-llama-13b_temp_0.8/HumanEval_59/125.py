

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while n % 2 == 0:
        n = n // 2
    p = 3
    largest = 1
    while p * p <= n:
        if n % p == 0:
            largest = p
            n = n // p
        else:
            p += 2

    if n > largest:
        largest = n

    return largest

