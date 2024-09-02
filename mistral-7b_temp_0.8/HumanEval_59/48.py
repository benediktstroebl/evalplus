

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        raise ValueError("No largest prime factor of negative integers or 1")

    # Determine largest prime factor
    num = n
    prime = n
    while prime > 1:
        while num % prime != 0:
            prime -= 1
        num = num // prime
        prime -= 1

    # Return largest prime factor
    return prime

