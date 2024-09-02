

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # we only need to try up to the square root of n to find the largest
    # prime factor
    i = 2
    while n % i != 0:
        i += 1

    while i * i <= n:
        while n % i == 0:
            n /= i
        i += 1
    return n

