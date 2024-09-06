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
    assert isinstance(n, int) and n > 0, "The input number must be integer greater than 0"

    def _factors(n: int, i: int) -> List[int]:
        if n % i == 0:
            return [i] + _factors(n // i, i)
        return []

    return _factors(n, 2)

