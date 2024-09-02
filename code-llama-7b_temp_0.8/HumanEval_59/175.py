

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # We loop through all odd numbers starting from 3 up to n/2.
    # If n is divisible by i, we can say that i is a prime factor.
    for i in range(3, int(n/2), 2):
        # If we find a factor, return it.
        if n % i == 0:
            return i

    # We could not find a factor, so the number is prime.
    return n

