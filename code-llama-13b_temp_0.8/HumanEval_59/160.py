

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_prime_factor = 1
    if n % 2 == 0:
        largest_prime_factor = 2
    while n % 2 == 0:
        n /= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            largest_prime_factor = i
            while n % i == 0:
                n /= i
    if n > largest_prime_factor:
        largest_prime_factor = n
    return int(largest_prime_factor)
