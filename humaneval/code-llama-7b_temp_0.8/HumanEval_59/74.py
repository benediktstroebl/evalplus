

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # The largest prime factor will be the last prime number that is less than
    # n
    last_prime = 1
    factor = 2

    # Iterate over the numbers between 2 and n
    while factor <= n:
        # If n is divisible by factor
        if n % factor == 0:
            # Set n to be n/factor and set last_prime to factor
            n = n/factor
            last_prime = factor
        else:
            # Increment factor by 1
            factor += 1
    return last_prime

