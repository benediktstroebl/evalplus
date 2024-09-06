

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Initialize the largest prime factor to 1, and increment it if we find a factor.
    # Initialize the largest prime factor to 1, and increment it if we find a factor.
    largest = 1
    i = 2

    # While i is less than or equal to n, increment i.
    while i <= n:
        # If n divided by i leaves no remainder, set n to be the largest prime factor.
        if n % i == 0:
            largest = n
            # Set n to be divided by i (the next potential largest prime factor).
            n = n // i
        # Otherwise, increment i.
        else:
            i += 1

    return largest
