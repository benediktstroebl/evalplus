

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # 2 is the largest prime factor of any number, but we'll loop once to be sure
    # the loop ends on a number that is greater than 1
    largest = 2
    while n % 2 == 0:
        largest = 2
        n //= 2

    factor = 3
    while n != 1 and factor * factor <= n:
        if n % factor == 0:
            largest = factor
            n //= factor
        else:
            factor += 2
    return largest
