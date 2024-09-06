

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return 2
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            for i in range(3, int(sqrt(n)) + 1, 2):
                if n % i == 0:
                    n = n // i
                    break
            else:
                return i
    return n