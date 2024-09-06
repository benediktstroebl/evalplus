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
    if n == 1:
        return factors

    # Find all factors of n.
    i, j = 2, n
    while i * i <= j:
        if n % i == 0:
            factors.append(i)
            j /= i
        else:
            i += 1

    if j > 1:
        factors.append(j)

    return factors

from collections import Counter
from typing import Tuple
