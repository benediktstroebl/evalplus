

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    for i in range(n - 1, 0, -1): # loop over values from n - 1 down to 1
        if n % i == 0: # if there is no remainder...
            return i # return the value
    return 1 # if there are no factors, return 1
