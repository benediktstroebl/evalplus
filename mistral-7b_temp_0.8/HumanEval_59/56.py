

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    n = abs(n)
    if n == 1:
        return 1
    else:
        for i in range(2, int(n ** 0.5) + 1):
            while n % i == 0:
                n = n / i
                if n == 1:
                    return i

