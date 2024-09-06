

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    limit = int(n ** 0.5)
    if limit % 2 == 0:
        limit -= 1
    while True:
        if n % 2 == 0:
            n = n // 2
            if n == 1:
                return 2
            elif n == 2:
                return 1
        else:
            limit -= 2
            for i in range(3, limit + 1, 2):
                if n % i == 0:
                    n = n // i
                    if n == 1:
                        return i
            return n

