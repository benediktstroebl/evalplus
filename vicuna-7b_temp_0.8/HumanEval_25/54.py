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
    if n < 2:
        return []
    if n == 2:
        return [2]
    factors = []
    for i in range(3, int(n**0.5) + 1, 2):
        for j in range(i**2, n+1, 2):
            if j % i == 0:
                break
        else:
            factors.append(i)
    remaining_factors = n - sum(i * (i-1) for i in factors)
    for i in remaining_factors:
        if i % 2 == 0:
            continue
        for j in factors:
            if i % j == 0:
                break
        else:
            factors.append(i)
    return factors
