

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    max_prime_factor = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if prime(i):
                max_prime_factor = i
            if prime(n // i):
                return largest_prime_factor(n // i)
    if prime(n):
        max_prime_factor = n
    return max_prime_factor

