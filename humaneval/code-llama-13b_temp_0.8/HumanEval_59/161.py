

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_prime = 1
    for i in range(2, n + 1):
        if n % i == 0:
            if n // i <= i:
                largest_prime = max(largest_prime, n // i)
            else:
                largest_prime = max(largest_prime, largest_prime_factor(n // i), i)

    return largest_prime

