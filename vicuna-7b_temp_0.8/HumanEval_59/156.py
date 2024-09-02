

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if not n > 1 or n % 2 == 0 or n % 3 == 0 or n % 4 == 0:
        return 1

    # Find the largest prime factor p less than sqrt(n)
    for i in range(5, int(np.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i

    # If no prime factor has been found, return 1
    return 1
