

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # while n is not prime, divide by its smallest prime divisor
    while n % 2 == 0:
        n = n // 2

    # now, n is odd, so only need to check odd divisors
    i = 3
    while i * i <= n:
        while n % i == 0:
            n = n // i
        i = i + 2

    return n
