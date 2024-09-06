

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while True:
        i = 0
        while i < len(str(n)) // 2 and n % 2 == 0:
            i += 1
        if n > 1 and n % 2 == 0:
            n = 2
        else:
            while n < n // 2:
                n += 1
            if n == n // 2:
                n += 1
            if n > 2 and n % 2 != 0:
                return n

    return n
