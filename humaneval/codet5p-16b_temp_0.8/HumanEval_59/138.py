

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    largest_prime = -1
    for k in range(2,n):
        if n % k == 0:
            if is_prime(k):
                largest_prime = k
    return largest_prime
