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
    from itertools import accumulate

    factors = []
    for k in range(2, n):
        if n % k == 0:
            factors.append(k)
    factors.sort()
    if len(factors) > 1:
        factors += [1] * (n - sum(factors))
    else:
        factors += [1] * n
    return
