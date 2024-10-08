

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    def is_prime(n: int):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    for i in range(2, n):
        if n % i == 0 and is_prime(i):
            largest = i
    return largest

