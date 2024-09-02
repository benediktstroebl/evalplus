

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Note: This method is not guaranteed to return the largest prime factor, but it is guaranteed to
    # return a prime factor.

    i = 2
    largest = 1
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            largest = i
    if n > largest:
        largest = n
    return largest

