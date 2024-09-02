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
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if j % i == 0:
                break
        else:
            factors.append(i)
    result = []
    while len(factors) > 1:
        i, j = factors.pop(0), factors.pop(0)
        if i % j == 0:
            while i % j == 0:
                i = i / j
                j = j - 1
            factors.append(i)
            result.append(i)
    return result