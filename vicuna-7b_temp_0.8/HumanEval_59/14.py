

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            continue
        if n % 3 == 0:
            n = 3 * n / 3
            continue
        for i in range(5, int(log(n) / log(2)) + 1):
            if n % i == 0:
                n = i * n / i
                continue
        break
    return n
