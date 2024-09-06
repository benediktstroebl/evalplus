

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # the second check is so that we don't get a divide by zero error when we
    # divide n
    largest_prime_factor = 2
    prime = 2
    # We stop when the current factor (prime) is greater than the number
    # the remaininig number to be factored (n). We do this so that we don't get
    # a zero divisor error
    while n > 1 and prime <= n:
        # check to see if prime divides n
        if n % prime == 0:
            # it does, so set n to be equal to its current factor (prime)
            n = n // prime
            largest_prime_factor = prime
        else:
            # it does not, so increase the current factor (prime) by one
            prime += 1
    return largest_prime_factor

