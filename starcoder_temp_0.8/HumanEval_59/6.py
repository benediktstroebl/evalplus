

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # 1 is the only even prime factor
    while n % 2 == 0:
        n = n // 2
    # 2 is the only even prime factor
    while n % 3 == 0:
        n = n // 3
    # Now we have a number that is only divisible by the primes 2 and 3.
    # Thus we can stop at sqrt(n) and check whether the number is divisible
    # by that number.
    sqrt_n = math.floor(math.sqrt(n))
    for i in range(5, sqrt_n + 1, 6):
        while n % i == 0:
            n = n // i
    return n
