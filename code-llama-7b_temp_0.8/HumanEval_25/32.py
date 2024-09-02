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
    from math import sqrt
    from itertools import groupby

    def factorize_aux(n, factors):
        for i in range(2, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                n /= i
                factors.append(i)
                break
        return n, factors

    if n < 1:
        raise ValueError("Only positive integers are allowed")
    factors = []
    while n > 1:
        n, factors = factorize_aux(n, factors)
    return list(map(int, list(map(lambda x: x[0], groupby(sorted(factors))))))

