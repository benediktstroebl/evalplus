

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    if n <= 1:
        return n
    elif is_prime(n):
        return n
    elif n % 2 == 0:
        return largest_prime_factor(n//2)
    else:
        return largest_prime_factor(n * 3 + 1)
