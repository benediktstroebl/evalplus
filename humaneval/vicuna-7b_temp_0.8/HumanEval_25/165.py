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
    def check(x):
        if x > 1:
            if x % 2 == 0:
                return False
            else:
                for y in range(3, x):
                    if x % y == 0:
                        return False
                return True
    factors = []
    while check(n):
        for x in range(2, n):
            if check(x):
                factors.append(x)
        n = n // 2
    return factors

