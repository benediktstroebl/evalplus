

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Return the largest prime factor of n
    def largest_prime_factor(n):
        return 1


    # For every n from 2 to n // 2, determine whether n % i is 0.
    # If so, then divide n by i and recurse with the result.
    # If n % i is not 0 for any i, return n.
    i = 2
    while i * i <= n:
        if n % i == 0:
            return largest_prime_factor(n // i)
        i += 1
    return n

    pass
