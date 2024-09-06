

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    #Hint: Check whether n is prime using a loop. If not, keep dividing it by its
    #largest prime factor.
    for i in range(2, n):
        if n % i == 0:
            n = n // i
    return n

