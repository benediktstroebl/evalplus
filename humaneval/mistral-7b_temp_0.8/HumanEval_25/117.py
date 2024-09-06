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
    factors = []

    def find_factors(n: int, factor: int = 2) -> None:
        """ Recursive function that finds factor of a given integer and adds it to list of factors """
        if n < factor:
            return

        if n % factor == 0:
            factors.append(factor)
            n //= factor
            return find_factors(n, factor)

        find_factors(n, factor + 1)

    find_factors(n)
    return factors
