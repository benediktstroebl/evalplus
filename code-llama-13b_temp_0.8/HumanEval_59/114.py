

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    largest_prime = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0 and n // i <= 1:
            largest_prime = i
    return largest_prime
