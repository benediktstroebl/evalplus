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
    def check(n):
        if n < 0:
            raise ValueError("n should be non-negative")
        if n == 0:
            return []
        if n == 1:
            return [n]

        for p in factorize(n // p):
            for i in range(1, len(p)):
                if p**i % n != 0:
                    return [p**i]
        return []

    n = int(n)
    result = check(n)
    return result

