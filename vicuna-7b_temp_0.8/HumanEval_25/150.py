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
    # check if n is prime
    if not n % 2:
        return [n]

    # if n is prime, check if it is greater than 3 and return its factors
    factors = []
    while n > 1:
        if n % 2 == 0:
            return [n]
        factors.append(n)
        n = n - 1
    return factors
