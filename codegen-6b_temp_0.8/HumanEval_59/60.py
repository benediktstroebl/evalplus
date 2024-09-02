

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 2
    max_i = int(n**0.5)
    # Continues to reduce n until sqrt is reached
    while i < max_i:
        if n % i == 0:
            max_i = i
            n //= i
        else:
            i += 1
    return n

