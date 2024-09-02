

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # it's always safe to test the first two primes for divisibility
    # for any integer greater than the square of the second prime
    # (which is the number of digits in the second prime).
    for i in (2, 3):
        if n % i == 0:
            return i
        while n % i == 0:
            n //= i
    for i in range(5, int(n ** 0.5) + 1, 6): # try 5, 11, 17, 23, ...
        if n % i == 0:
            return i
        if n % (i + 2) == 0:
            return n // (i + 2)
    return n
