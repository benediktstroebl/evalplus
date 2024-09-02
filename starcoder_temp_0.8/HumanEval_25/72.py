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

    def factorize_recursive(number: int, result: List[int] = []) -> List[int]:
        """ Return list of prime factors of given integer in the order from smallest to largest.
        Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
        Input number should be equal to the product of all factors """
        if number == 1:
            return result
        for factor in range(2, number + 1):
            if number % factor == 0:
                result.append(factor)
                return factorize_recursive(number // factor, result)
        return result

    return factorize_recursive(n)

