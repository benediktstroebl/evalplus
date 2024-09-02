

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    p = 5
    while n > 1 and n % p == 0:
        n //= p
        p += 6
    return n if n <= 1 else n - 1
