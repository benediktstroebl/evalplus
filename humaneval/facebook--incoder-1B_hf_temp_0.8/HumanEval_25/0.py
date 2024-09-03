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
    if n % 2 == 0:
        raise ValueError(f'The input number should be even. Input number: {n}')
    factors = []
    factors.append(1)
    while n > 1:
        for k in range(2, n + 1):
            if n % k == 0:
                factors.append(k)
                break
        n = n // k
    return factors

