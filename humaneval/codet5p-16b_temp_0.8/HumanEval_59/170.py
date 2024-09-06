

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n < 2:
        return None
    else:
        largest_prime = 0
        i = 2
        while i < n:
            if n % i == 0:
                n //= i
                largest_prime = i
            else:
                i += 1
        return largest_prime

