

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    i = 2
    while n > 1:
        if n % i == 0:
            n = n / i
        else:
            i += 1
    return i

