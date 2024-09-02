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
    assert n >= 2

    # base case
    if n == 2:
        return [2]

    # Check if n is prime.
    if n % 2 == 0:
        return [2] + factorize(n // 2)

    # recursively find next highest prime factor.
    return [n] + factorize(n - 1)
