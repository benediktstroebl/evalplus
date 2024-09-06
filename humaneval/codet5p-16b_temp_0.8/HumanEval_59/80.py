

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    max = n
    i = 2
    while i < max:
        if n % i == 0:
            max = n // i
            if max % 2 == 0:
                return max
            return i
        i += 1
    return 1

