

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    if n % 2 == 0:
        if n == 2:
            return n
        else:
            return 2
    prime = 3
    while n > 1:
        if n % prime == 0:
            return prime
        else:
            prime += 2

