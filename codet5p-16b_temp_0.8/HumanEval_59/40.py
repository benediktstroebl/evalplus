

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n == 1:
        return 1
    max_prime = 2
    while n > 1:
        max_prime += 1
        while n % max_prime!= 0:
            max_prime += 1
        n /= max_prime
    return max_prime
