

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    #getting quotient of n with largest prime factor
    largest_factor = 1
    #getting quotient of n with 2
    while n % 2 == 0:
        largest_factor = 2
        n = n / 2
    #getting quotient of n with odd numbers starting from 3
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n = n / i
    #if n is a prime number
    if n > 2:
        largest_factor = n
    return largest_factor

