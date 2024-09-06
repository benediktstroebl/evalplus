

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while True:
        if not n % 2:
            if n % 2 == 0:
                return 2
        elif not n % 3:
            if n % 3 == 0:
                return 3
        elif not n % 5:
            if n % 5 == 0:
                return 5
        elif not n % 7:
            if n % 7 == 0:
                return 7
        else:
            break

    return n
