

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # factor divisor down until we hit a prime
    for divisor in range(2, n + 1):
        # check if divisor divides n evenly
        if n % divisor == 0:
            # update n to be the quotient
            n //= divisor
            # check if the quotient is 1 or prime
            if n == 1:
                # return the most recent divisor
                return divisor
            # otherwise, check if the new quotient is prime
            elif largest_prime_factor(n) == 1:
                # if so, return the previous divisor
                return divisor

