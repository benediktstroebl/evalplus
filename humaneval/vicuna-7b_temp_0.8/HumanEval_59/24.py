

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n <= 1:
        raise ValueError("n should be positive")
    if n % 2 == 0:
        return 2
    while True:
        i = 2
        while True:
            if n % i == 0:
                break
            i += 2
        if n > i:
            break
        n = i
    while n > 3:
        d = 1
        while d % n == 0:
            d *= n
        n = d * (n - d)
    return n