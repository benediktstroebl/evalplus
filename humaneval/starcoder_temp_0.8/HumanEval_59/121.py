

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    assert n > 1
    # loop through all factors of n
    for i in range(2, n+1):
        # if n is divisible by i
        if n % i == 0:
            # check if i is prime
            if is_prime(i):
                # if it is, return i
                return i

    return -1
