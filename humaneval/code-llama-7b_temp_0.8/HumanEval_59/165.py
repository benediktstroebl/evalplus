

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Keep dividing by 2 as long as we can
    # 2 is the largest prime smaller than sqrt(n)
    while n % 2 == 0:
        n /= 2

    # Check all odd numbers down to sqrt(n)
    # as they can never be divisible by a number
    # larger than sqrt(n)
    i = 3
    while i * i <= n:
        while n % i == 0:
            n /= i
        i += 2

    return int(n)

