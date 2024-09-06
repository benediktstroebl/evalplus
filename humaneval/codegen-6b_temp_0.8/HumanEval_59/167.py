

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n % 2 == 0:
        return 2
    else:
        if n % 3 == 1:
            return 3
        else:
            i = 5
            while n % i != 0:
                i += 2
            return i

