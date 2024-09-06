

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # keep dividing the number by the largest factor
    # for now, this will be the first factor we find
    largest_factor = 2

    # once n gets to be less than the largest factor we have found,
    # we know that this must be our largest prime factor
    while n > largest_factor:

        # divide n by the largest factor
        n = n // largest_factor

        # look for a new largest factor
        largest_factor = largest_prime_factor_between_one_and(n)

    return largest_factor

