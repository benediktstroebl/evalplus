

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    largest_prime_factor = 1

    while n % 2 == 0:
        largest_prime_factor = 2
        n = n / 2

    for num in range(3, n + 1, 2):
        while n % num == 0:
            largest_prime_factor = num
            n = n / num

    return largest_prime_factor
