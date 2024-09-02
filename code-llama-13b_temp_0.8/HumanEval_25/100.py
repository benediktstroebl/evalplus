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

    def helper(i: int, n: int, factors: List[int]):
        if n == 1 or i == n + 1:
            return factors
        if n % i == 0:
            return helper(i + 1, n // i, factors + [i])
        else:
            return helper(i + 1, n, factors)

    return helper(2, n, [])

