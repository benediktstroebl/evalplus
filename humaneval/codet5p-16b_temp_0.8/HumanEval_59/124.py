

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n <= 1:
        raise ValueError("Input must be greater than 1")
    max_factor = n - 1
    while max_factor > 1:
        if is_prime(max_factor):
            return max_factor
        max_factor -= 1
