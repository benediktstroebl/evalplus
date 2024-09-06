from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n < 1:
        return []
    if n == 1:
        return [1]
    factors = []
    while n > 1:
        # Get the first prime number bigger than sqrt(n)
        p = get_prime(n)
        # Get the list of factors
        factors = get_factors(n, p, factors)
        # Reduce n
        n //= p
    return factors

