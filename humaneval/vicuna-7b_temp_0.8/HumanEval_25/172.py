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
    factorization = []
    while n > 1:
        i = 0
        while i < len(factorization) and n % factorization[i]:
            i += 1
        if i == len(factorization):
            break
        while n % factorization[i]:
            n /= factorization[i]
        factorization.append(n % factorization[i])
    return factorization

