

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    def helper(n, i, prime_factors):
        if n == 1:
            return prime_factors
        elif n % i == 0:
            return helper(n // i, 2, prime_factors + [i])
        else:
            return helper(n, i + 1, prime_factors)
    return helper(n, 2, [])[-1]


