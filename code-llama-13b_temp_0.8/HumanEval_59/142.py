

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime = 1
    # YOUR CODE HERE
    while n > 2:
        if n % 2 == 0:
            prime = 2
            n = n // 2
        else:
            n += 1
    return prime

