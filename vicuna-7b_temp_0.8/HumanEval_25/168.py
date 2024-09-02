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
    def get\_factors(n: int) -> List[int]:
        """ Return list of prime factors of given integer. """
        factors = []
        while n > 1:
            n = n - 1
            if n % 2 == 0:
                break
        factors.append(2)
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                break
        while n % i != 0:
            i += 1
        factors.extend((i for i in range(3, int(n**0.5) + 1, 2) if n % i == 0))
        return factors

    return get\_factors(n)[1:] # removing first factor

