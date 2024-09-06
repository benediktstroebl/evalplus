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
    factor = [1]
    i = 1
    while i < n:
        for j in range(1, i + 1):
            if i % j == 0:
                factor.append(j)
                i = i / j
                break
        else:
            factor.append(i)
            i = 1
    
