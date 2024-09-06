

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    pf = 1
    for i in range(2, n + 1):
        if n % i == 0:
            pf = i
            n = int(n / i)
            while (n % i == 0):
                n = int(n / i)
            if n == 1:
                break
    return pf

