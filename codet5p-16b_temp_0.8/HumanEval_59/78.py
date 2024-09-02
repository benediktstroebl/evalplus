

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    max_prime = 2 # start with 2 since 1 is not a prime
    if n < 2:
        raise ValueError("Invalid input")
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                n //= i
                max_prime = i
                break
    return max_prime
