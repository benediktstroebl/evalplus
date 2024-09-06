

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n < 2:
        raise ValueError("Expected n > 1 but got {0}".format(n))
    largest = 0
    while n % 2 == 0:
        largest = 2
        n = n / 2
    for i in range(3, n + 1, 2):
        while n % i == 0:
            largest = i
            n = n / i
    return largest
