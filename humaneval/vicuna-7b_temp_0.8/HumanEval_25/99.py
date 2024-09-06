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
    # check if n is prime
    if n > 1:
        if n % 2 == 0:
            return []
        for i in range(3, int(n**0.5) + 1, 6):
            if n % i == 0:
                return []
    factors = []
    for i in range(1, int(n**0.5) + 1, 6):
        if n % i == 0:
            break
        factors.append(i)
    for i in range(6, int(n**0.5) + 1, 6):
        if n % i == 0:
            continue
        for j in range(i, n):
            if n % j == 0:
                break
            factors.append(j)
    return factors

