

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Keep dividing n by prime factors of n, until it is a prime number.
    largest_prime_factor = 1
    for i in range(2, n + 1):
        if n % i == 0:
            largest_prime_factor = i
            while n % i == 0:
                n = n // i
            # After dividing n by i, if n is prime, then we are done.
            if n == 1:
                return largest_prime_factor

    # If we reach this point, then n was a prime number.
    return n
