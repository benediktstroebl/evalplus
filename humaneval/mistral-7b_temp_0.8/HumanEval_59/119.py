

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Start with 2.
    i = 2
    # Loop through increasing values of i until we find
    # the largest prime factor.
    while n > 1:
        # Check if i is a factor of n.
        if n % i == 0:
            # If it is, divide n by i.
            n //= i
        # Otherwise, increment i to the next prime number.
        else:
            i += 1
    return i

