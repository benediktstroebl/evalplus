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
    while n != 1:
        for i in range(2, n):
            if i not in factors:
                if n % i == 0:
                    break
            if i in factors:
                if n % i != 0:
                    break
            factors[i] += 1
    result = []
    for key, value in factors.items():
        if value > 1:
            result.append(key)
            result.append(value)
    return result

