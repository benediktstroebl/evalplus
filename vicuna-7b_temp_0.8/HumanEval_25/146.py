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
    # Check for 0 or 1
    if n < 2:
        return [n]
    # Check for prime
    if n > 2:
        p = 2
        while p**2 <= n:
            p += 2
        return [p]
    # Check for composite
    for i in range(2, n):
        for j in range(i**2, n, i):
            if j % i == 0:
                return [i, j]
    return []
