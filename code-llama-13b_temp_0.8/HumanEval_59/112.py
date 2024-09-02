

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # By inspection, we observe that 2 is the largest prime factor.
    largest_prime = 2
    while n % largest_prime == 0:
        n //= largest_prime
    # We need to test odd numbers only from 3 to sqrt(n).
    # All other factors will pair with a factor less than sqrt(n).
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n //= i
    if n > 2:
        largest_prime = n
    return largest_prime

