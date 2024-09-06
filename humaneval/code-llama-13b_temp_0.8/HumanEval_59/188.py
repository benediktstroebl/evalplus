

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_factor = -1
    while n % 2 == 0:
        prime_factor = 2
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            prime_factor = i
            n = n // i
    if n > 2:
        prime_factor = n
    return prime_factor

