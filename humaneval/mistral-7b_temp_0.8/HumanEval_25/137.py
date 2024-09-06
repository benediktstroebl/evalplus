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

    def factorize_helper(n: int, factor: int = 2, factor_list: List[int] = factors):
        if n == 1:
            return factor_list
        if n % factor == 0:
            factor_list.append(factor)
            return factorize_helper(n // factor, factor, factor_list)
        return factorize_helper(n, factor + 1, factor_list)

    factors = factorize_helper(n)
    return factors

