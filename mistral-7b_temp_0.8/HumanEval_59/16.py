

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    assert n > 1, "n must be greater than 1"

    # TODO: Implement this function
    result = 1
    while n % result != 0:
        result += 1

    return result - 1
