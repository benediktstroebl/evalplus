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
    sqrt = n ** 0.5
    nfactors = 1
    limit = int(sqrt)
    result = []
    while nfactors * limit < n:
        if n % (limit + 1) == 0:
            nfactors += 1
            result.append(limit + 1)
            n /= (limit + 1)
        else:
            limit -= 1
    if nfactors * limit == n:
        result.append(limit)
    result.sort()
    return result

