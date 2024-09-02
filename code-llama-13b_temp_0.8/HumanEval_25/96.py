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
    factor = []
    for i in range(2, n + 1):
        while n % i == 0:
            factor.append(i)
            n //= i
        i += 1
    return factor

    # Another way
    # factors = []
    # i = 2
    # while n > 1:
    #     if n % i == 0:
    #         factors.append(i)
    #         n = n // i
    #     else:
    #         i += 1
    # return factors

