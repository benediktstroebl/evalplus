

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Check for prime by using trial division
    if n < 3:
        raise ValueError("n must be greater than 2")
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            raise ValueError("n must be prime")
    return n
