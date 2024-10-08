

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    max_prime = -1
    while n % 2 == 0:
        max_prime = 2
        n = n / 2
    for i in range(3, n + 1, 2):
        while n % i == 0:
            max_prime = i
            n = n / i
    return max_prime
