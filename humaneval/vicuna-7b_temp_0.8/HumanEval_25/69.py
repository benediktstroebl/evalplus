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
    def dfs(n, p, factors):
        if n == 1:
            return [p] + factors
        for i in range(1, n):
            factors.append(p * i)
            dfs(n - i, p * i, factors + [p])
        return factors

    factors = []
    for i in range(1, n + 1):
        p = 2
        dfs(n, p, factors)
    return factors
