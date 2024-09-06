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
    count = 0

    for k in range(1, n + 1):
        if n % k == 0:
            factors.append(k)
            count += 1
    factor = 1
    for i in range(0, count):
        factor = factor * factors[i]
    if factor == n:
        return factors
    else:
        raise ValueError("Input number should be equal to the product of all factors")

