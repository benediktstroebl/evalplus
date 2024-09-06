

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    small_prime = 2
    while n % small_prime != 0:
        small_prime = get_next_prime(small_prime)
    return small_prime

