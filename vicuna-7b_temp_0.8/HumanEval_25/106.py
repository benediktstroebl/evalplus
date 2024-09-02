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
    factors = [2]
    while n > 1:
        while n % 2 == 0:
            n = n // 2
        for x in range(3, int(n**0.5) + 1, 2):
            if n % x == 0:
                n = x
                break
        factors.append(n)
    return factors
