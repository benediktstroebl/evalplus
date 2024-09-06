

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # check if n is even
    while n % 2 == 0:
        n //= 2
    # check if n is odd
    while n % 3 == 0:
        n //= 3
    for i in range(5, int(n**0.5)+1, 6):
        while n % i == 0:
            n //= i
        while n % (i+2) == 0:
            n //= (i+2)
    return n
