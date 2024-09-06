

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    max_prime_factor = 1
    for prime in prime_list:
        if n % prime == 0:
            n = n // prime
            max_prime_factor = prime
    return max_prime_factor

