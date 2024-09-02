

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_factor = 0
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factor = i
    return n if n > prime_factor else prime_factor


