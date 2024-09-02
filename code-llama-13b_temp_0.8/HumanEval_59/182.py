

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_prime = 1
    if n % 2 == 0:
        while n % 2 == 0:
            largest_prime = 2
            n = n // 2

    k = 3
    while k * k <= n:
        if n % k == 0:
            largest_prime = k
            while n % k == 0:
                n = n // k

        k += 2

    if n > 2:
        largest_prime = n

    return largest_prime
