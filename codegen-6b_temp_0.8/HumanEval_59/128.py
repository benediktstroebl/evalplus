

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    curr = n
    i = 2
    while i < curr:
        if curr % i == 0:
            if is_prime(i):
                curr = curr / i
        i += 1
    return curr
