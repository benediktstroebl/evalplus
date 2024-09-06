

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # a new variable for the prime factor. This variable will be modified.
    prime_factor = 2
    # a variable to keep track of the current loop iteration
    counter = 2

    while prime_factor <= n and counter < n // prime_factor:
        prime_factor = n // counter
        counter += 1

    return prime_factor

