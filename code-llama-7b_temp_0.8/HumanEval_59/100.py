

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_prime = 2
    while n % 2 == 0:
        largest_prime = 2
        n //= 2

    # start with 3 and go up by 2.
    # Keep going until you have found the largest prime factor.
    p = 3
    while n % p == 0:
        largest_prime = p
        n //= p
    # Above while loop will skip out if n is prime.
    return largest_prime
