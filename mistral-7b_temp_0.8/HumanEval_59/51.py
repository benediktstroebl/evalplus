

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # YOUR CODE HERE
    # initialize variables
    largest_prime_factor_so_far = 1
    for factor in range(2, int(n**0.5) + 1):
        while n % factor == 0:
            largest_prime_factor_so_far = factor
            n /= factor
        if largest_prime_factor_so_far > 1:
            break

    if n > 1:
        largest_prime_factor_so_far = n

    return largest_prime_factor_so_far

