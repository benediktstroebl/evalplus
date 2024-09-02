

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Hint: Try Fermat's factorization method
    # first try 2 as a factor
    # if it is, divide n by 2
    # if not try 3
    # if it is, divide n by 3
    # if not, try 5
    # if it is, divide n by 5
    # and so on
    i = 2
    while n > i:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n






