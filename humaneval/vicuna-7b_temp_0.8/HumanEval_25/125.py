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
    factors = {}
    for i in range(1, n + 1):
        for factor in range(i, n + 1):
            if factor not in factors:
                factors[factor] = 1
            factors[factor] += 1
        if factors:
            for key, value in factors.items():
                if value > 1:
                    yield key
                    yield -key
    if factors:
        for key, value in factors.items():
            if value > 1:
                yield key
                
