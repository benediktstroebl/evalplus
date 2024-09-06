

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # base case
    if n % 2 == 0:
        return 2
    # recursive case
    if n % 2 == 1:
        return largest_prime_factor(n - 1)

