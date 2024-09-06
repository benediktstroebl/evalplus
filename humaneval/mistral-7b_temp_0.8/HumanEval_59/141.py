

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # TODO: Implement the function.
    assert n > 1, "Not a positive number"
    if n % 2 == 0:
        return 2
    while True:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                n = n // i
                return i

