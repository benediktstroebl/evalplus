

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    if n < 2:
        return None
    for i in range(n):
        if n % (i+1) == 0:
            if is_prime(i+1):
                return i+1
