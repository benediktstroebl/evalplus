

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # I did not come up with this solution. It is an improved version
    # of the solution in the book.
    divisor = 2
    candidate = divisor
    while n % candidate != 0:
        candidate += 1
        if candidate >= n:
            divisor = 3
            candidate = divisor
    # Loop breaks when candidate is prime
    return candidate

